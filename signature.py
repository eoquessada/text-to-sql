import dspy 

class GenerateSQL(dspy.Signature):
    """
    Generates SQL queries given a business question.
    """

    question: str = dspy.InputField(
        description="Business question."
    )

    sql_query: str = dspy.OutputField(
        description="SQL query."
    )