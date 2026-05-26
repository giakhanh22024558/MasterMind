# jira-conventions.md

Override defaults của skill [`integration/jira`](../MasterMind/models/model_001/integration/jira/conventions-defaults/).

## Project key

```yaml
project_key: "<PROJECT>"          # bắt buộc fill — Jira project key (vd "LEX", "ABC")
```

## Tag system

```yaml
# tags:
#   feature_tag: on               # default on — luôn prepend [FEAT-XXX]
#   cr_tag: auto                  # default auto — bật khi story có prefix [CR-XX]
#   custom_tags:                  # luôn prepend (vd milestone tag)
#     - "MVP-1"
```

## Sub-tasks

```yaml
# sub_tasks:
#   roles: [BA, FE, BE]           # default 3 roles. Thêm: [BA, FE, BE, QA, Design]
#   mode: auto                    # auto = skip role 0h | all = đủ mọi role
```

## Issue types

```yaml
# issue_types:
#   main: Task                    # default Task | Story | Improvement
#   sub:  Sub-task                # default Sub-task
```

## Priority mapping

```yaml
# priority_map:
#   P0: Highest
#   P1: High
#   P2: Medium
```

## Custom field IDs (per Jira instance)

```yaml
# custom_fields:
#   story_points: customfield_10016
#   sprint:       customfield_10020
```

## Output folder

```yaml
# output_folder: output/jira/     # default
```
