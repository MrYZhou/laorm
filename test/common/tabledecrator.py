from laorm import FieldDescriptor, sql, table


@table("config")
class Config1:
    id: str = FieldDescriptor(primary=True)
    name: str = FieldDescriptor()

    @sql
    def selectByName(name: str) -> list["Config1"]:
        pass


print(Config1.selectByName(123))
