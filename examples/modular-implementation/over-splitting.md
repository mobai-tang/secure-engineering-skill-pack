# Bad Output: Over-Splitting

The agent splits a cohesive 40-line transformation into six tiny files only to satisfy a belief that more files are more modular.

## Better Behavior

Keep the cohesive transformation together unless extraction creates a real ownership boundary, isolates independent change, enables reuse or focused testing, or matches established repository structure.
