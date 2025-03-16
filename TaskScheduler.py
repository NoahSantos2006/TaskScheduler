class TaskScheduler(object):
    def __init__(self, and_dependencies, or_dependencies):
        self.and_dependencies = and_dependencies
        self.or_dependencies = or_dependencies

        #initializes the successors
        self.all_successors = {key: set() for key in and_dependencies}
        for key, value in self.and_dependencies.items():
            for value1 in value:
                self.all_successors[value1].add(key)
        for key, value in self.or_dependencies.items():
            for value1 in value:
                self.all_successors[value1].add(key)

        #initializes the predecessors
        self.all_predecessors = {key: set() for key in and_dependencies}
        for key, value in self.all_successors.items():
            for value1 in value:
                self.all_predecessors[value1].add(key)

        # initializes available tasks
        self.available_tasks = set()
        for key, value in self.all_successors.items():
            if self.all_successors[key] and (not self.and_dependencies[key] and not self.or_dependencies[key]):
                self.available_tasks.add(key)
        
        #initializes remaining tasks
        self.remaining_tasks = set(key for key in self.and_dependencies.keys())

    def get_remaining_tasks(self):
        return self.remaining_tasks

    def get_available_tasks(self):
        return self.available_tasks

    def complete_task(self, task):
        if task not in self.available_tasks:
            print("That task is not avaailable")
        else:

            #updates available and remaining tasks
            self.available_tasks.discard(task)
            self.remaining_tasks.discard(task)
            
            #updates successors
            del self.all_successors[task]
            
            #updates predecessors
            for key, value in self.all_predecessors.items():
                if task in value:
                    self.all_predecessors[key].remove(task)
            del self.all_predecessors[task]

            #updates dependencies
            for key, value in self.or_dependencies.items():
                if task in value:
                    print(self.or_dependencies, "BEFORE")
                    value.remove(task)
                    print(self.or_dependencies, "AFTER")
                    if key in self.remaining_tasks:
                        self.available_tasks.add(key)

            for key, value in self.and_dependencies.items():
                if task in value:
                    value.remove(task)
                    if not value and key in self.remaining_tasks:
                        self.available_tasks.add(key)
        
    def all_tasks_completed(self):
        return not self.remaining_tasks

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
