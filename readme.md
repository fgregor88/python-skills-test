# Python Skills Test

The aim of this project is to assess the user's Python skills, starting from the basics to advanced topics. After the skill assessment, the project should recommend further learning resources to improve the user's skills.

This is a terminal application.

The application should generate problems for the user to solve one by one and, after each problem, the solution should be evaluated, critiqued, and rated. If the problem was successfully solved, the application will continue generating new problems (maximum of 5 in total). If the user is unable to solve the current problem, the application stops testing and continues with the recommendation/learning part.

## Additional Clarifications

- **Target audience**: Is this intended for complete beginners, intermediate users, or a mix of levels?
- **Problem types**: Should problems focus only on core Python (syntax, data structures, functions, OOP), or also include topics like file I/O, modules, testing, and third-party libraries?
- **Evaluation method**: Should solutions be evaluated automatically (e.g., via unit tests and static checks) or is there a human-in-the-loop scenario?
- **Difficulty progression**: Should difficulty strictly increase with each problem, or can it adapt dynamically based on performance (e.g., easier if the user struggles)?
- **Persistence**: Do we need to store user results and learning recommendations (e.g., in a file or database) for later review?
- **Learning recommendations**: Should recommendations be generic (e.g. "read about lists") or link to specific resources (articles, courses, docs), and if so, do you have preferred sources?
- **Runtime constraints**: Should we assume the user has only standard Python installed, or can we rely on additional dependencies (e.g., `rich` for nicer terminal UI)?