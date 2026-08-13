# Glossary — Thuật ngữ nghiệm thu

Tài liệu này dùng cho đội phát triển và người thẩm định. Mục tiêu là để hai nhóm
độc lập có thể áp dụng cùng tiêu chí và lưu cùng loại bằng chứng.

## Claim cốt lõi

- **Định nghĩa:** phát biểu kiến thức mà nếu sai, thiếu điều kiện hoặc bị hiểu
  sai sẽ làm thay đổi mục tiêu, cách giải thích, hoạt động, đáp án hoặc quyết
  định của người học.
- **Cách xác nhận:** người soạn đánh dấu khi lập bản đồ kiến thức; một giáo viên
  môn học duyệt lại.
- **Bằng chứng lưu:** claim, vị trí trong bài, nguồn/vị trí hỗ trợ và điều kiện áp
  dụng.
- **Ngoại lệ:** lời dẫn, câu chuyển ý và hướng dẫn tổ chức không phải claim cốt
  lõi trừ khi chứa kiến thức hoặc yêu cầu an toàn.

## Cảnh báo nghiêm trọng

- **Định nghĩa:** lỗi phải chặn phát hành, gồm claim cốt lõi bị nguồn phủ định,
  câu hỏi không có đáp án hợp lệ, câu hỏi ngoài phần đã dạy, rò rỉ secret/dữ
  liệu học sinh, vi phạm quyền sử dụng đã biết hoặc hướng dẫn gây nguy hiểm.
- **Cách xác nhận:** rule tự động hoặc reviewer nêu bằng chứng; giáo viên/chủ sở
  hữu dữ liệu quyết định cách sửa, không được chỉ bấm bỏ qua không lý do.
- **Bằng chứng lưu:** mã cảnh báo, artifact/vị trí, nguồn hoặc policy liên quan,
  người xử lý, quyết định và thời điểm.
- **Ngoại lệ:** false positive chỉ được đóng khi có lý do và bằng chứng lưu lại.

## Một vòng sửa có kiểm soát

- **Định nghĩa:** một chu kỳ gồm bản đầu vào cố định → reviewer ghi nhận xét →
  tác giả/AI sửa → reviewer chấp nhận hoặc mở lại lỗi.
- **Cách đo:** lưu thời điểm bắt đầu/kết thúc, diff theo block và danh sách cảnh
  báo đóng/mở.
- **Ai xác nhận:** reviewer của vòng đó.
- **Ngoại lệ:** sửa lỗi chính tả hàng loạt không được tính là một vòng nghiệp vụ
  riêng.

## Tỷ lệ nội dung phải viết lại

- **Đơn vị:** block có nghĩa sư phạm, ví dụ đoạn giải thích, hoạt động, câu hỏi,
  đáp án hoặc tiêu chí rubric; không đo chỉ bằng số từ.
- **Block được tính là viết lại:** bị xóa/thay thế; đổi kết luận; đổi mục tiêu;
  hoặc thay trên 30% nội dung để dùng được.
- **Công thức:** `số block phải viết lại / tổng block AI tạo`.
- **Bằng chứng lưu:** diff block, thời gian chỉnh sửa chủ động và lý do sửa.
- **Ngoại lệ:** định dạng, chính tả và đổi cách xưng hô không tính nếu không đổi
  nghĩa; vẫn theo dõi thời gian riêng.

## Học sinh hoàn thành mục tiêu

- **Định nghĩa:** đạt ngưỡng đã đặt trước trên nhiệm vụ trực tiếp đo mục tiêu,
  không suy ra từ tổng điểm chung.
- **Pilot Vật lí 10:**
  - Mục tiêu 1: đúng ít nhất 2/3 nhận định chuyển hóa và có giải thích.
  - Mục tiêu 2: sửa được quan niệm sai về ma sát, nêu cả cơ năng và nhiệt năng.
  - Mục tiêu 3: thiết lập đúng bảo toàn cơ năng và hoàn thành ít nhất một bài
    tính đơn giản với đơn vị.
- **Ai xác nhận:** giáo viên dạy theo đáp án/rubric thống nhất trước tiết học.
- **Bằng chứng lưu:** bài làm đã ẩn danh, rubric và bối cảnh lớp.

## Đã được giáo viên duyệt (`Teacher-reviewed`)

- **Định nghĩa:** một giáo viên đúng môn/cấp học đã đọc đủ bốn nhóm đầu ra và
  hoàn thành rubric.
- **Bằng chứng:** rubric, nhận xét, phiên bản package và danh tính/vai trò người
  duyệt theo mức công khai đã đồng ý.
- **Ngoại lệ:** tác giả tự duyệt bài của mình không đủ để gắn trạng thái này.

## Đã được đồng nghiệp duyệt (`Peer-reviewed`)

- **Định nghĩa:** tối thiểu hai giáo viên đúng môn/cấp học chấm độc lập trước
  khi thảo luận; mọi bất đồng được ghi và giải quyết.
- **Bằng chứng:** hai rubric ban đầu, biên bản bất đồng, quyết định sửa và phiên
  bản cuối.
- **Ngoại lệ:** hai reviewer cùng chấm trong một cuộc họp mà không có kết quả
  độc lập không đạt trạng thái này.

## Đã thử nghiệm trong lớp (`Classroom-tested`)

- **Định nghĩa pilot:** bài đã được dạy ít nhất hai lần ở ít nhất hai lớp; có bối
  cảnh, thời lượng, thiết bị, kết quả mục tiêu và ghi nhận thay đổi sau mỗi lần.
- **Ai xác nhận:** giáo viên dạy và người phụ trách nghiên cứu/pilot.
- **Bằng chứng:** biểu mẫu bối cảnh, dữ liệu đã ẩn danh, phiên bản bài, sự cố và
  thay đổi sau dạy.
- **Ngoại lệ:** dạy thử cho đồng nghiệp hoặc demo không học sinh không tính.

