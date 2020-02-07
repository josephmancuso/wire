from orator.migrations import Migration


class CreateTodosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('todos') as table:
            table.increments('id')
            table.string('name')
            table.string('description')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('todos')
