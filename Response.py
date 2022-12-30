from datetime import datetime


def sample_response(input):
    user_mess = str(input).lower()

    if user_mess in ("hi", "hello", "ok"):
        return "Chào bạn, tôi có thể giúp gì cho bạn không?"

    if user_mess in ("time", "time?"):
        now = "Hôm nay là: " + datetime.now().strftime("%d-%m-%y, %H:%M:%S")
        return str(now)

    if user_mess in "bye":
        return "Tạm biệt, hẹn gặp lại nhé!"

    if user_mess in "fb":
        return "Chào bạn, tôi có thể giúp gì cho bạn không?"

    if user_mess in "phòng thư viện ở đâu?":
        return "Phòng thư viện ở lầu D tầng 3"

    if user_mess in "trang web của thư viện":
        return "Đây là link của trang web thư viện: https://lic.ut.edu.vn/"

    if user_mess in "làm thẻ thư viện như thế nào?":
        return "Bạn cần một hình thẻ và 60 nghìn tiền làm thẻ."

    if user_mess in "trang web của trường":
        return "Đây là link trang web của trường: https://ut.edu.vn/"

    if user_mess in "trang web của Viện chất lượng cao":
        return "Đây là link của viện chất lượng cao: http://clc.ut.edu.vn/"

    if user_mess in ("trang web của sinh viên", "làm sao để đăng nhập vào trang sinh viên"):
        return "Đây là link của trang web của sinh viên: https://sv.ut.edu.vn/"

    if user_mess in "hệ thống đào tạo trực truyến":
        return "Đây là link của trang web đào tạo trực tiếp: https://courses.ut.edu.vn/"

    if user_mess in "hệ thống thi trực tuyến":
        return "Đây là link của trang web thi trực tiếp: https://exam.ut.edu.vn/"

    if user_mess in "trường bao bao nhiêu cơ sở":
        return "Trường có 3 cơ sở: Cơ sở 1: Số 2, Đường Võ Oanh, P.25, Q. Bình Thạnh, Thành Phố Hồ Chí Minh, " \
               "Cơ sở 2: Số 17 đường số 12, Trần Não, P. Bình An, TP. Thủ Đức, TP. HCM, Cơ sở 3: Số 70 đường Tô Ký, " \
               "phường Tân Chánh Hiệp, quận 12, TP. Hồ Chí Minh, Cơ sở 4: TP. Vũng Tàu: số 17A đường 3-2, P.11, " \
               "TP. Vũng Tàu, Cơ sở Đồng Nai (xã Long Đức, huyện Long Thành, Đồng Nai):  20 ha đất, đang xây dựng. "

    if user_mess in "phó hiệu trưởng là ai":
        return "Phó hiệu trưởng là Lê Văn Lang. Thông tin chi tiết https://ut.edu.vn/articles/ban-giam-hieu-16.html"

    if user_mess in "hiệu trưởng là ai":
        return "Hiệu trưởng là Nguyễn Xuân Phương. Thông tin chi tiết https://ut.edu.vn/articles/ban-giam-hieu-16.html"

    if user_mess in "trường có bao nhiêu khoa, viện, trung tâm, bộ môn quản lý đào tạo":
        return "Các khoa, viện, trung tâm, bộ môn quản lý đào tạo: Bộ môn Giáo dục quốc phòng - An ninh & Giáo dục " \
               "thể chất, Khoa Công nghệ thông tin, Khoa Cơ bản, Khoa Điện - Điện tử viễn thông, Khoa Kinh tế vận " \
               "tải, Khoa Lý luận chính trị, Viện Cơ khí, Viện Hàng hải, Viện Xây dựng, Viện Ngôn ngữ và Khoa học xã " \
               "hội. "
    if user_mess in "trường có bao nhiêu phòng, ban, trung tâm chức năng":
        return "Các phòng, ban, trung tâm chức năng: Phòng Công tác sinh viên, Phòng Đào tạo, Phòng Đối ngoại, Phòng " \
               "Kế hoạch – Tài vụ, Phòng Khoa học và hợp tác quốc tế, Phòng Quản trị cơ sở vật chất, Phòng Quản lý " \
               "chất lượng, Phòng Tổ chức – Hành chính, Trung tâm Thông tin - Thư viện, Viện Đào tạo Sau đại học."

    if user_mess in (
            "trường có bao nhiêu tổ chức nghiên cứu và phát triển, đơn vị sự nghiệp, cơ sở sản xuất, kinh doanh, "
            "dịch vụ"):
        return "Các tổ chức nghiên cứu và phát triển, đơn vị sự nghiệp, cơ sở sản xuất, kinh doanh, dịch vụ: " \
               "Tạp chí Khoa học công nghệ và giao thông vận tải, Trung tâm NCKH & phát triển công nghệ giao thông " \
               "vận tải, Trung tâm Nhân lực và huấn luyện hàng hải, Trung tâm Ngôn ngữ, CNTT và đào tạo nghiệp vụ, " \
               "Trung tâm Đào tạo và bồi dưỡng nghiệp vụ giao thông vận tải, Trung tâm Đào tạo thường xuyên, Viện Giao " \
               "thông Việt Nga, Viện Đào tạo Chất lượng cao, Viện Đào tạo & Hợp tác quốc tế, Phòng thí nghiệm " \
               "LAS-XD313. "

    if user_mess in "trường có bao nhiêu tổ chức chính trị - xã hội":
        return "Tổ chức chính trị - xã hội: Đảng bộ, Công đoàn trường, Đoàn thanh niên - Hội sinh viên, Hội Cựu chiến " \
               "binh . "

    if user_mess in "ký túc xá ở đâu":
        return "Ký túc xá ở số 10 đường số 12, KP3, P. An Khánh, TP. Thủ Đức, TP. HCM"

    if user_mess in ("hồ sơ nhập học cần những cái gì", "nhập học thì cần những cái gì"):
        return "Thí sinh cần mang theo bản sao những loại hồ sơ sau: Giấy chứng nhận đối tượng ưu tiên tuyển sinh(nếu " \
               "có), Sổ khổ khẩu(nếu là đối tượng ưu tiên tuyển sinh 01), Giấy khai sinh(nếu là đối tượng ưu tiên " \
               "tuyển sinh 01,06), Chứng minh nhân dân hoặc Căn cước công dân(Để làm Thẻ sinh viên tích hợp thẻ ngân " \
               "hàng Vietcombank), Thẻ bảo hiểm ý tế(Để nhà trường lấy dữ liệu làm thẻ mới hoặc để làm minh chứng đối " \
               "với trường hợp thuộc diện gia đình được nhà nước cấp thẻ BHYT). Ngoài ra thí sinh cần chuẩn bị ảnh " \
               "thẻ phông nền trắng để có thể làm một số công việc như sau: 1 ảnh 4x6(làm thẻ sinh viên nếu không có " \
               "file mềm), 6 ảnh 3x4(ký túc xá, xác nhận làm thẻ xe buýt,...), 2 ảnh 2x3(gia nhập Hội sinh viên," \
               "...). Trường hợp thí sinh là đoàn viện cần mang theo sổ đoàn viên để chuyển sinh hoạt đoàn về đoàn " \
               "thanh niên trường. "

    if user_mess in "làm sao để đăng ký ở tại ký túc xá":
        return "Tân sinh viên có như cầu đăng ký Ký túc xá liên hệ trực tiếp Bộ phận quản lý ký túc xá tại cơ sở " \
               "thành phố Phủ Đức. "

    if user_mess in "trường bao nhiêu tiền 1 tín chỉ":
        return "Trường trình đào tạo đại trà trình độ đại học: 354.000 đồng/chỉ. Trường trình chất lượng cao trình độ " \
               "đại học: 770.000 đồng/chỉ. "

    if user_mess in "gmail của trường đại học gia thông vận tải":
        return "gmail của trường đại học gia thông vận tải là: ut-hcmc@ut.edu.vn"

    if user_mess in "thời gian các tiết học":
        return "thời gian học chia làm 4 ca: ca 1 tiết 1-3, ca 2 tiết 4-6, ca 3 tiết 7-9, ca 4 tiết 10-12. Thông tin " \
               "chi tiết xem thêm ở đây: https://clc.ut.edu.vn/thoi-gian-day-hoc-dh-chinh-quy/ "
    if user_mess in "đi học quân sự thì cần mang những cái gì":
        return "Bạn cần mang theo: Gối, dầu gội, bột gặt, thuốc (thuốc đau đầu, sốt, ho, thuốc đau bụng), ổ cắm, " \
               "chăn(nếu học vào thời tiết lạnh, quân khu sẽ phát chăn nhưng mỏng), giày, bút và vở. "

    if user_mess in "trang web của khoa công nghệ thông tin":
        return "Đây là trang web của Khoa CNTT: https://it.ut.edu.vn/"

    if user_mess in "trang web của khoa điện":
        return "Đây là trang web của Khoa Điện: http://dtvt.ut.edu.vn/"

    if user_mess in "trang web của khoa kinh tế vận tải":
        return "Đây là trang web của Khoa Kinh tế vận tải: https://kinhte.ut.edu.vn/"

    if user_mess in "trang web của viện hàng hải":
        return "Đây trang web của Viện hàng hải: http://ma.ut.edu.vn/"

    if user_mess in "trang web của viện cơ khí":
        return "Đây trang web của Viện Cơ khí :https://ime.ut.edu.vn/"

    if user_mess in "trang web của viện xây dựng":
        return "Đây trang web của Viện Xây dựng: https://ice.ut.edu.vn/"

    if user_mess in "trang web của viện ngôn ngữ và khoa học xã hội":
        return "Đây trang web của Viện ngôn ngữ và khoa học xã hội: https://ilass.ut.edu.vn/"

    if user_mess in "trang web của phòng công tác sinh viên":
        return "Đây trang web của phòng Công tác sinh viên: http://gts.edu.vn/"

    if user_mess in "trang web của phòng đào tạo":
        return "Đây trang web của phòng Đào tạo: http://daotao.ut.edu.vn/"

    if user_mess in "trang web của phòng khoa học và hợp tác quốc tế":
        return "Đây trang web của phòng Khoa học và hợp tác quốc tế: https://sicd.ut.edu.vn/"

    if user_mess in "trang web của phòng thanh tra và quản lý chất lượng":
        return "Đây trang web của phòng thanh tra và quản lý chất lượng: http://qm.ut.edu.vn/"

    if user_mess in "trang web của viện đào tạo sau đại học":
        return "Đây trang web của Viện đào tạo sau đại học: http://sdh.ut.edu.vn/"

    if user_mess in "trang web của viện năng lượng và giao thông":
        return "Đây trang web của Viện năng lượng và giao thông: http://ioet.edu.vn/"

    if user_mess in "trang web của viện đào tạo và hợp tác quốc tế":
        return "Đây trang web của Viện đào tạo và hợp tác quốc tế: http://iec.ut.edu.vn/vi/trang-chu/"

    if user_mess in "trường có những câu lạc bộ nào":
        return "Trường có các câu lạc bộ là: Câu lạc bộ Sách và hành động, Câu lạc bộ Taekwondo, Câu lạc bộ Giai điệu " \
               "trái tim, Câu lạc bộ Kỹ năng, Câu lạc bộ Vovinam, Câu lạc bộ Truyền thông, Câu lạc bộ Âm nhạc khoa " \
               "kinh tế vận tải, Câu lạc bộ Bóng rổ, Câu lạc bộ Khởi nghiệp, Đội công tác xã hội, Câu lạc bộ Sống " \
               "đẹp, Câu lạc bộ Anh văn, Câu lạc bộ Bóng đá, Câu lạc bộ Thể thao điện tử,... "

    if user_mess in "fanpage của trường đại học giao thông vận tải":
        return "Đây là fanpage của trường: https://www.facebook.com/TruongDHGiaothongvantaiTPHCM"
    return "Lệnh sai rồi, vui lòng kiểm tra lại!"
