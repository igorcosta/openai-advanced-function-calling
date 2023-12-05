from utils.functions_metadata import function_schema


@function_schema(
    name="find_staff",
    description="Find staff member by first and last name",
    required_params=["first_name", "last_name"]
)
def find_staff(first_name: str, last_name: str):
    """
    :param first_name: Staff first name to appear in the search
    :param last_name: Staff last name to appear in the search
    """
    return f"Staff member {first_name} {last_name} found"
