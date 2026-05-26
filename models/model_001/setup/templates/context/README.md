# context/

**Agent-managed** `.md` sidecars cho mọi file trong `input/` và `output/`.

## Purpose

Đọc `.md` rẻ hơn `.docx` / `.xlsx` rất nhiều (~10x token savings). Mỗi binary file phải có 1 sidecar tương ứng trong folder này.

## Convention

```
input/SRS_v1.docx          → context/SRS_v1.md
input/Issues_MS1.xlsx      → context/Issues_MS1.md
output/<project>-SRS.docx  → context/<project>-SRS.md
```

Agent tự tạo sidecar khi:
- Đọc binary file lần đầu (`"đọc context của <file>"`)
- Mỗi lần tạo binary output (`"render SRS"` → tự tạo cả sidecar)
- User trigger explicit sync (`"sync drive"`, `"refresh context"`)

## Rules

- ❌ User KHÔNG edit thủ công — sẽ bị overwrite next sync
- ✅ User chỉ READ để tham khảo content
- ✅ Agent tự overwrite khi có version mới của source
- ❌ Đừng commit folder này vào MasterMind git — per-project, không phải skill content
