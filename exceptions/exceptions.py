class DifferentSizeVectors(Exception):
    def __init__(self, *args: object) -> None:
        self.message = f"Vectors must have the same lenght"
