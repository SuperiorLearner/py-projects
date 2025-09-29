import json
from pathlib import Path

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.file = Path(filename)
        self.todos = json.loads(self.file.read_text()) if self.file.exists() else []
    
    def save(self):
        if self.todos:
            self.file.write_text(json.dumps(self.todos, indent=2))
        elif self.file.exists():
            self.file.unlink()
    
    def add(self, task):
        self.todos.append({"id": max((t['id'] for t in self.todos), default=0) + 1, "task": task, "done": False})
        self.save()
        print(f"✓ Added task #{self.todos[-1]['id']}")
    
    def list(self, f="all"):
        todos = [t for t in self.todos if f == "all" or (f == "pending" and not t['done']) or (f == "done" and t['done'])]
        if not todos: return print(f"No {f} tasks!")
        print(f"\nYour Tasks ({f}):")
        [print(f"  [{'✓' if t['done'] else ' '}] {t['id']}. {t['task']}") for t in todos]
    
    def toggle(self, id):
        for t in self.todos:
            if t['id'] == id:
                t['done'] = not t['done']
                self.save()
                return print(f"✓ Task #{id} {'completed' if t['done'] else 'reopened'}")
        print(f"Task #{id} not found")
    
    def delete(self, id):
        l = len(self.todos)
        self.todos = [t for t in self.todos if t['id'] != id]
        if len(self.todos) < l: 
            self.save()
            print(f"✓ Deleted task #{id}")
        else: 
            print(f"Task #{id} not found")
    
    def run(self):
        print("=== Simple Todo App ===\nCommands: add <task> | list [all/pending/done] | done <id> | delete <id> | quit\n")
        while True:
            try:
                inp = input("> ").strip().split(maxsplit=1)
                if not inp: continue
                cmd, arg = inp[0].lower(), inp[1] if len(inp) > 1 else None
                match cmd:
                    case 'quit' | 'q' | 'exit': return print("Goodbye!")
                    case 'add' if arg: self.add(arg)
                    case 'list': self.list(arg.lower() if arg else "all")
                    case 'done' if arg and arg.isdigit(): self.toggle(int(arg))
                    case 'delete' if arg and arg.isdigit(): self.delete(int(arg))
                    case _: print("Invalid command")
            except (KeyboardInterrupt, EOFError): return print("\nGoodbye!")
            except Exception as e: print(f"Error: {e}")

if __name__ == "__main__":
    TodoApp().run()