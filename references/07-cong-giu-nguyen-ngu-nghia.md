# Cổng giữ nguyên ngữ nghĩa

Chạy sau mọi lượt viết lại, humanize hoặc áp persona. Mục tiêu là ngăn câu chữ tự nhiên hơn nhưng
kiến thức sai đi.

## Inventory phải khóa

Trước khi sửa, liệt kê hoặc trích máy các mục sau nếu có:

- claim và trạng thái `supported / unsupported / contradicted`;
- citation, source ID và locator;
- số liệu, đơn vị, khoảng, dấu bất đẳng thức và mức làm tròn;
- công thức, ký hiệu, biến và điều kiện áp dụng;
- quan hệ nguyên nhân, ngoại lệ, mức độ chắc chắn;
- câu hỏi, lựa chọn, đáp án và claim ID tương ứng;
- thuật ngữ bắt buộc, code, URL, slug và định danh máy.

## So sánh sau khi sửa

Chặn đầu ra nếu xảy ra một trong các thay đổi không được phép:

- thêm claim mới hoặc biến suy luận thành sự thật;
- bỏ điều kiện làm câu rộng nghĩa hơn;
- đổi “có thể” thành “sẽ”, “thường” thành “luôn”, tương quan thành nguyên nhân;
- đổi số, dấu, đơn vị, công thức, đáp án hoặc citation;
- ví dụ mâu thuẫn với quy tắc nó minh họa;
- persona tuyên bố trải nghiệm/chuyên môn không có căn cứ;
- rút gọn làm mất một bước cần thiết để hiểu cơ chế hay thực hiện nhiệm vụ.

Nếu cần thay đổi một mục đã khóa vì phát hiện lỗi, quay lại bước nguồn/claim và ghi đó là sửa nội
dung có chủ đích. Không ngụy trang nó thành chỉnh văn phong.

## Kết quả kiểm tra

Ghi ngắn một trong ba trạng thái nội bộ:

- `PASS`: inventory không đổi và artifact vẫn đúng chức năng.
- `REVISE`: ý đúng nhưng mất điều kiện, mắt xích hoặc độ rõ; sửa rồi kiểm lại.
- `BLOCK`: phát sinh claim/đáp án/citation không có căn cứ; quay lại nguồn hoặc yêu cầu thẩm định.
