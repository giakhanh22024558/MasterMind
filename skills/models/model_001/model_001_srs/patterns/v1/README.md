# model_001_srs · patterns

Pattern tái sử dụng cho việc sinh tài liệu SRS.

## Available patterns

| Pattern | Mục đích |
|---|---|
| [`content-format-separation.md`](content-format-separation.md) | Tách nội dung (.md) khỏi hình thức (Python); kéo theo các quy ước tự sinh (mã ID, số hình, numbering) |

## How to add a new pattern

1. Tạo `<pattern-name>.md` trong thư mục này
2. Theo cấu trúc: **Problem → Solution → Trade-offs → Worked example → When NOT to use → Cross-references**
3. Nếu pattern là instantiation của một [meta-pattern](../../../../../../meta/), reference ngược về meta-pattern thay vì lặp lại

## When to promote a pattern to `meta/`

Nếu một pattern xuất hiện ở 3+ skill → không còn skill-specific. Promote lên [`meta/`](../../../../../../meta/) theo [defer-then-promote pattern](../../../../../../meta/defer-then-promote-pattern/).
