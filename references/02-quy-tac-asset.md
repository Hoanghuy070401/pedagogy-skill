<!-- Nguồn: schoolAI-deploy/website/STUDIO-ASSET-RULES.md (copy nguyên bản).
     Dùng được gần như nguyên vẹn ở dự án khác; chỉ thay "Studio", "Storage theo release" và
     "validator" bằng tên pipeline/cổng phát hành tương ứng của dự án bạn. -->

# Quy tắc asset Studio — minh hoạ bằng code trước

Áp dụng cho mọi proposal, revision và release do Studio tạo.

## Quy tắc mặc định

1. AI phải ưu tiên block minh hoạ sinh từ code/JSON: Mermaid, SVG có kiểm soát, CSS, sơ đồ hoặc component đã đăng ký. **Code/JSON chỉ là nguồn biên soạn; renderer phải biến nó thành hình/sơ đồ trực quan cho học viên, không hiển thị mã nguồn trừ khi bài đang dạy chính mã đó.**
2. Không dùng ảnh raster (ảnh pixel như PNG, JPG, WebP, AVIF) chỉ để trang trí hoặc thay cho một sơ đồ có thể render bằng code.
3. Ảnh raster chỉ được đề xuất khi người học cần thấy giao diện thật: ảnh chụp IDE, vị trí nút/menu, màn cài đặt, thao tác thiết bị hoặc trạng thái phần mềm không thể mô tả đúng bằng block code.

## Điều kiện dùng ảnh raster

Mỗi ảnh phải có `reason` giải thích vì sao không thể thay bằng minh hoạ sinh từ code, cùng `alt`, caption, `width`, `height`, `mimeType`, `contentHash` và tham chiếu Storage theo release. Ảnh phải cắt đúng vùng cần học, không chứa dữ liệu cá nhân/secret và không lặp asset cùng hash.

## Cổng phát hành

- Validator từ chối asset raster thiếu trường bắt buộc hoặc `reason` rỗng.
- Preview phải render block minh hoạ thành hình thật ở desktop và mobile; nếu chỉ hiện text/code/JSON thì fail gate.
- Validator từ chối GIF/video cho minh hoạ thông thường; ngoại lệ cần owner phê duyệt, fallback tĩnh và mô tả chữ.
- Mobile chỉ tải asset của track/bài người học chọn offline. Mỗi release phải kiểm tra budget asset trước publish.
- Nếu mobile không render được animation/interactive, release phải có block fallback giữ mục tiêu học và cách tự kiểm.
