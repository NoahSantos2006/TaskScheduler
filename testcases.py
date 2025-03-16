add_dependencies = {'a': {'b', 'c'}, 'b':set(), 'c':set(), 'b1': set(), 'b2': set(), 'c1': set(), 'c2': set()}
or_dependencies = {'a':set(), 'b': {'b1', 'b2'}, 'c': {'c1', 'c2'}, 'b1': set(), 'b2': set(), 'c1': set(), 'c2': set()}
s = TaskScheduler(add_dependencies, or_dependencies)
assert s.get_available_tasks() == {'b1', 'b2', 'c1', 'c2'}
s.complete_task('b1')
assert s.get_available_tasks() == {'b', 'b2', 'c1', 'c2'}
s.complete_task('b')
assert s.get_available_tasks() == {'b2', 'c1', 'c2'}
s.complete_task('c1')
assert s.get_available_tasks() == {'b2', 'c', 'c2'}
s.complete_task('c')
assert s.get_available_tasks() == {'b2', 'a', 'c2'}

add_dependencies = {'a': set(), 'b':{'b1','b2'}, 'c':{'c1','c2'}, 'b1': set(), 'b2': set(), 'c1': set(), 'c2': set()}
or_dependencies = {'a': {'b','c'}, 'b': set(), 'c': set(), 'b1': set(), 'b2': set(), 'c1': set(), 'c2': set()}
s = TaskScheduler(add_dependencies, or_dependencies)
assert s.get_available_tasks() == {'b1', 'b2', 'c1', 'c2'}
s.complete_task('b1')
assert s.get_available_tasks() == {'b2', 'c1', 'c2'}
s.complete_task('c1')
assert s.get_available_tasks() == {'b2', 'c2'}
s.complete_task('c2')
assert s.get_available_tasks() == {'b2', 'c'}
s.complete_task('c')
assert s.get_available_tasks() == {'b2', 'a'}

print("Test case: Pass")