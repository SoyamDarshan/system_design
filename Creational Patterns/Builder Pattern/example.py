# Implement builder pattern to print code blocks
class CodeBuilder:
    def __init__(self, root_name):
        self.class_name = root_name
        self.class_attributes = []

    def add_field(self, type, name):
        self.class_attributes.append('    self.{} = {}'.format(type, name))
        return self

    def __str__(self):
        if len(self.class_attributes) > 0:
            return 'class {}:'.format(self.class_name) + '\n' + '  def __init__(self):' + '\n' + '\n'.join(
                self.class_attributes)
        else:
            return 'class {}:'.format(self.class_name) + '\n' + '  pass'


cb = CodeBuilder('Person').add_field('name', '""') \
    .add_field('age', '0')
print(cb)

cb = CodeBuilder('Person')
print(cb)
