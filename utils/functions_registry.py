import importlib.util
import os
from pathlib import Path
import json
import logging
from typing import Optional, Dict, List

logger = logging.getLogger(__name__)


class FunctionsRegistry:
    def __init__(self) -> None:
        self.functions_dir = Path(__file__).parent.parent / 'functions'
        self.registry: Dict[str, callable] = {}
        self.schema_registry: Dict[str, Dict] = {}
        self.load_functions()

    def load_functions(self) -> None:
        if not self.functions_dir.exists():
            logger.error(
                f"Functions directory does not exist: {self.functions_dir}")
            return

        for file in self.functions_dir.glob('*.py'):
            module_name = file.stem
            if module_name.startswith('__'):
                continue

            spec = importlib.util.spec_from_file_location(module_name, file)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if callable(attr) and hasattr(attr, 'schema'):
                        self.registry[attr_name] = attr
                        self.schema_registry[attr_name] = attr.schema

    def resolve_function(self, function_name: str, arguments_json: Optional[str] = None):
        func = self.registry.get(function_name)
        if not func:
            raise ValueError(f"Function {function_name} is not registered.")

        try:
            if arguments_json is not None:
                arguments_dict = json.loads(arguments_json) if isinstance(
                    arguments_json, str) else arguments_json
                return func(**arguments_dict)
            else:
                return func()
        except json.JSONDecodeError:
            logger.error("Invalid JSON format.")
            return None
        except Exception as e:
            logger.error(f"Error when calling function {function_name}: {e}")
            return None

    def mapped_functions(self) -> List[Dict]:
        return [
            {
                "type": "function",
                "function": func_schema
            }
            for func_schema in self.schema_registry.values()
        ]

    def get_function_callable(self):
        # Return a dictionary mapping function names to their callable functions
        return {func_name: func for func_name, func in self.registry.items()}

    def generate_schema_file(self) -> None:
        schema_path = self.functions_dir / 'function_schemas.json'
        with schema_path.open('w') as f:
            json.dump(list(self.schema_registry.values()), f, indent=2)

    def get_registry_contents(self) -> List[str]:
        return list(self.registry.keys())

    def get_schema_registry(self) -> List[Dict]:
        return list(self.schema_registry.values())
