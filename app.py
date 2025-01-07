from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

# Hàm trả lời ngẫu nhiên
def bot_response(user_input):
    responses = {
        "xin chào": [
            "xin chào",
            "chào bạn tôi có thể giúp gì cho bạn"
        ],    
        "hello": [
            "xin chào tôi có thể giúp gì bạn",
            "chào bạn tôi có thể giúp bạn học tiếng anh bạn sẵn sàng chứ"
        ],
        "giới thiệu": [
            "chatbot này giúp bạn luyện tập tiếng anh trả lời các câu hỏi liên quan đến từ vựng ngữ pháp và các chủ đề học tiếng anh cơ bản",
            "tôi là một chatbot luôn sẵn sàng hỗ trợ bạn cải thiện tiếng anh qua các câu hỏi và bài tập"
        ],
        "cách học tiếng anh": [
            "học từ vựng và ngữ pháp là cách tốt nhất để xây dựng nền tảng tiếng anh vững chắc",
            "luyện nghe và nói hàng ngày sẽ giúp bạn cải thiện khả năng giao tiếp nhanh chóng",
            "sử dụng ứng dụng học tiếng anh là một phương pháp hiệu quả để luyện tập bất kỳ lúc nào",
            "học qua bài hát và phim là cách thú vị để cải thiện kỹ năng nghe và mở rộng từ vựng",
            "sử dụng flashcards là một cách tuyệt vời để ghi nhớ và ôn lại từ vựng một cách hiệu quả"
        ],
        "sách học tiếng anh": [
            "sách 'english grammar in use' là một trong những cuốn sách nổi tiếng giúp bạn cải thiện ngữ pháp tiếng anh",
            "cuốn 'word power made easy' là lựa chọn tuyệt vời để nâng cao vốn từ vựng tiếng anh của bạn",
            "'english vocabulary in use' sẽ giúp bạn học từ vựng theo các chủ đề rất phù hợp cho người học ở mọi trình độ",
            "sách 'the elements of style' cung cấp những quy tắc quan trọng giúp bạn viết tiếng anh một cách rõ ràng và chính xác",
            "'listening practice through dictation' là cuốn sách hữu ích để bạn cải thiện khả năng nghe và viết chính tả tiếng anh"
        ],
        "bạn có thể làm gì": [
            "tôi có thể giúp bạn luyện tập từ vựng cấu trúc câu và cải thiện khả năng phát âm tiếng anh",
            "tôi có thể trả lời câu hỏi của bạn về các chủ đề học tiếng anh"
        ],
        "làm sao để học tiếng anh hiệu quả": [
        "học tiếng anh hiệu quả là kiên trì luyện tập và tìm phương pháp học phù hợp",
        "bạn nên bắt đầu từ những kiến thức cơ bản sau đó dần dần nâng cao dần"
        ],
        "cách học từ vựng tiếng anh": [
            "học từ vựng qua flashcards và ôn lại đều đặn sẽ giúp bạn nhớ lâu",
            "lặp lại từ vựng thường xuyên và học theo chủ đề sẽ giúp bạn ghi nhớ tốt hơn"
        ],
        "cách cải thiện kỹ năng nghe tiếng anh": [
            "luyện nghe qua các bài hát, phim và podcast tiếng anh là cách tốt để cải thiện kỹ năng nghe",
            "thực hành nghe mỗi ngày và chú ý đến cách phát âm của người bản ngữ"
        ],
        "cách học ngữ pháp tiếng anh": [
            "học ngữ pháp qua sách và làm bài tập ngữ pháp sẽ giúp bạn củng cố kiến thức",
            "áp dụng ngữ pháp vào thực tế khi nói và viết để ghi nhớ lâu hơn"
        ],
        "cách luyện phát âm tiếng anh": [
            "luyện phát âm qua các video hướng dẫn phát âm của người bản ngữ là rất hữu ích",
            "bạn có thể ghi âm lại giọng nói của mình và so sánh với người bản ngữ để cải thiện"
        ],
        "có nên học tiếng anh qua bài hát": [
            "học qua bài hát giúp bạn cải thiện kỹ năng nghe và phát âm, đồng thời tạo sự hứng thú khi học",
            "chọn bài hát với tốc độ chậm và từ vựng dễ hiểu để dễ dàng tiếp thu"
        ],
        "cách học tiếng anh giao tiếp": [
            "tham gia vào các nhóm học tiếng anh hoặc tìm đối tác để luyện giao tiếp thường xuyên",
            "bạn nên tập trung vào các câu giao tiếp cơ bản và sử dụng chúng trong các tình huống thực tế"
        ],
        "làm sao để nhớ lâu từ vựng": [
            "áp dụng phương pháp spaced repetition để ôn lại từ vựng một cách hiệu quả",
            "học từ vựng theo hình ảnh hoặc liên kết với các kỷ niệm cá nhân sẽ giúp bạn ghi nhớ lâu hơn"
        ],
        "bài học tiếng anh cho người mới bắt đầu": [
            "bạn có thể bắt đầu học tiếng anh với các bài học về từ vựng cơ bản và cấu trúc câu đơn giản",
            "học từ vựng theo chủ đề giúp bạn dễ dàng ghi nhớ và áp dụng vào thực tế"
        ],
        "tiếng anh giao tiếp cơ bản": [
            "học các câu hỏi và câu trả lời đơn giản giúp bạn giao tiếp dễ dàng trong các tình huống hằng ngày",
            "luyện tập các câu giao tiếp như 'how are you?', 'where are you from?' sẽ giúp bạn tự tin hơn"
        ],
        "phương pháp học tiếng anh hiệu quả cho người bận rộn": [
            "bạn có thể học qua ứng dụng tiếng anh trong thời gian rảnh để tối ưu thời gian học",
            "học mỗi ngày một ít, sử dụng từ vựng và ngữ pháp trong thực tế sẽ giúp bạn học hiệu quả"
        ],
        "có nên học tiếng anh qua xem phim": [
            "xem phim là cách thú vị để cải thiện kỹ năng nghe và học từ vựng theo ngữ cảnh",
            "bạn nên xem phim có phụ đề tiếng anh để hiểu rõ hơn về từ vựng và cách phát âm"
        ],
        "cách tăng khả năng viết tiếng anh": [
            "bạn nên viết thường xuyên và nhờ người khác kiểm tra để cải thiện kỹ năng viết",
            "cải thiện khả năng viết bằng cách học các mẫu câu và cấu trúc câu tiếng anh thông dụng"
        ],
        "cách học tiếng anh giao tiếp với người bản ngữ": [
            "tham gia các câu lạc bộ tiếng anh hoặc tìm bạn bản ngữ để luyện giao tiếp",
            "bạn có thể thực hành giao tiếp với người bản ngữ qua ứng dụng trò chuyện hoặc video call"
        ],
        "cách phát âm chuẩn tiếng anh": [
            "học phát âm theo từ điển tiếng anh có phát âm chuẩn và luyện tập thường xuyên",
            "chú ý đến các âm vị trong tiếng anh như âm 'th', 'r', và 'l' để phát âm chuẩn hơn"
        ],
        "làm sao để cải thiện kỹ năng đọc tiếng anh": [
            "đọc sách tiếng anh và bài báo là cách tuyệt vời để cải thiện kỹ năng đọc",
            "bạn nên đọc các bài viết có từ vựng phù hợp với trình độ của mình để không bị choáng ngợp"
        ],
        "có thể học tiếng anh qua trò chơi không": [
            "trò chơi học tiếng anh sẽ giúp bạn học mà không cảm thấy nhàm chán và giúp ghi nhớ lâu",
            "bạn có thể chơi các trò chơi từ vựng hoặc ngữ pháp trên các ứng dụng học tiếng anh"
        ],
        "có nên học tiếng anh với giáo viên": [
            "học tiếng anh với giáo viên giúp bạn được chỉnh sửa phát âm và ngữ pháp ngay lập tức",
            "bạn có thể tham gia các lớp học trực tuyến hoặc học qua video với giáo viên để cải thiện nhanh chóng"
        ],
        "phương pháp học từ vựng hiệu quả": [
            "phương pháp học từ vựng qua flashcards và ôn tập định kỳ rất hiệu quả",
            "học từ vựng theo các chủ đề như gia đình, công việc, du lịch sẽ giúp bạn nhớ nhanh hơn"
        ],
        "tại sao phải học tiếng anh": [
            "tiếng anh là ngôn ngữ quốc tế giúp bạn giao tiếp và mở rộng cơ hội nghề nghiệp",
            "học tiếng anh giúp bạn tiếp cận với nhiều nguồn tài liệu học tập và giải trí phong phú"
        ],
        "làm sao để học tiếng anh nhanh chóng": [
            "học tiếng anh mỗi ngày và tạo thói quen sử dụng tiếng anh trong cuộc sống hàng ngày sẽ giúp bạn tiến bộ nhanh chóng",
            "học qua các ứng dụng tiếng anh hoặc tham gia lớp học giúp bạn học hiệu quả hơn"
        ],
        "có nên học tiếng anh qua sách vở": [
            "sách vở cung cấp nền tảng vững chắc về ngữ pháp và từ vựng, giúp bạn học tiếng anh hệ thống hơn",
            "bạn có thể kết hợp học sách với thực hành giao tiếp để phát huy hiệu quả tối đa"
        ],
        "có nên học tiếng anh qua podcast": [
            "học tiếng anh qua podcast giúp bạn luyện nghe và cải thiện khả năng hiểu ngữ điệu tự nhiên của người bản ngữ",
            "bạn có thể nghe podcast tiếng anh mỗi ngày để cải thiện kỹ năng nghe của mình"
        ],
        "cách học tiếng anh cho người mới bắt đầu": [
            "bạn nên bắt đầu với các bài học cơ bản về từ vựng và ngữ pháp, rồi nâng cao dần",
            "học tiếng anh mỗi ngày một chút và thực hành giao tiếp sẽ giúp bạn nhanh chóng cải thiện"
        ],
        "các tài liệu học tiếng anh tốt nhất": [
            "sách 'english grammar in use' và 'english vocabulary in use' là những tài liệu tuyệt vời giúp bạn học tiếng anh",
            "bạn cũng có thể sử dụng các ứng dụng học tiếng anh như Duolingo, Babbel để luyện tập mỗi ngày"
        ],
        "làm sao để nhớ từ vựng lâu dài": [
            "lặp lại từ vựng hàng ngày và liên kết từ vựng với hình ảnh hoặc tình huống sẽ giúp bạn nhớ lâu",
            "sử dụng từ vựng trong các câu và tình huống thực tế sẽ giúp bạn ghi nhớ lâu dài"
        ],
        "có nên tham gia khóa học tiếng anh online": [
            "khóa học online giúp bạn học tiếng anh linh hoạt và tiết kiệm thời gian",
            "nhiều khóa học tiếng anh online cung cấp tài liệu chất lượng và giảng viên giỏi"
        ],
        "do": [
            "Động từ 'do' được dùng để diễn tả hành động làm cái gì đó, ví dụ: 'I do my homework every day' (Tôi làm bài tập mỗi ngày).",
            "'Do' còn được sử dụng trong câu hỏi, ví dụ: 'Do you like coffee?' (Bạn thích cà phê không?).",
            "Trong câu phủ định, 'do' được sử dụng như 'I do not understand' (Tôi không hiểu).",
            "'Do' cũng có thể dùng để nhấn mạnh hành động trong câu, ví dụ: 'I do want to go!' (Tôi thực sự muốn đi!)."
        ],
        "make": [
            "'Make' diễn tả hành động tạo ra hoặc sản xuất cái gì đó, ví dụ: 'She makes a cake every Sunday' (Cô ấy làm bánh mỗi Chủ nhật).",
            "Cụm từ 'make a decision' có nghĩa là đưa ra quyết định, ví dụ: 'We need to make a decision soon' (Chúng ta cần đưa ra quyết định sớm).",
            "'Make a mistake' có nghĩa là mắc lỗi, ví dụ: 'I made a mistake in the test' (Tôi đã mắc lỗi trong bài kiểm tra).",
            "'Make' còn có thể diễn tả việc tạo ra một điều kiện hay sự kiện, như 'make an appointment' (hẹn gặp)."
        ],
        "get": [
            "'Get' có thể chỉ sự nhận, ví dụ: 'I get a gift on my birthday' (Tôi nhận quà vào ngày sinh nhật).",
            "'Get' cũng có thể chỉ sự di chuyển đến một nơi nào đó, ví dụ: 'I get to work at 9 AM' (Tôi đến công ty lúc 9 giờ sáng).",
            "'Get' còn diễn tả sự thay đổi trạng thái, ví dụ: 'I get tired after working' (Tôi mệt mỏi sau khi làm việc).",
            "'Get' còn dùng để diễn tả việc đạt được cái gì đó, ví dụ: 'She got the job' (Cô ấy đã có được công việc)."
        ],
        "go": [
            "'Go' chỉ sự di chuyển, ví dụ: 'I go to school by bus' (Tôi đi học bằng xe buýt).",
            "'Go on' có nghĩa là tiếp tục, ví dụ: 'The meeting will go on for an hour' (Cuộc họp sẽ tiếp tục trong một giờ).",
            "'Go ahead' có thể có nghĩa là tiếp tục hoặc bắt đầu, ví dụ: 'Go ahead and start without me' (Hãy bắt đầu mà không có tôi).",
            "'Go' cũng có thể diễn tả sự thay đổi trạng thái, ví dụ: 'The weather is going bad' (Thời tiết đang xấu đi)."
        ],
        "see": [
            "'See' có nghĩa là nhìn thấy, ví dụ: 'I see the sun rising' (Tôi thấy mặt trời mọc).",
            "'See' cũng có thể được dùng trong các tình huống gặp gỡ, ví dụ: 'I will see you tomorrow' (Tôi sẽ gặp bạn vào ngày mai).",
            "'See' còn được dùng để diễn tả sự hiểu biết, ví dụ: 'Now I see what you mean' (Bây giờ tôi hiểu bạn muốn nói gì).",
            "'See' trong một số cụm từ có nghĩa là xem xét hoặc thẩm định, ví dụ: 'Let's see what happens' (Hãy xem chuyện gì sẽ xảy ra)."
        ],
        "know": [
            "'Know' chỉ sự hiểu biết hoặc quen thuộc, ví dụ: 'I know the answer' (Tôi biết câu trả lời).",
            "'Know' còn có thể diễn tả sự quen biết với một ai đó, ví dụ: 'I know him very well' (Tôi rất quen anh ấy).",
            "'Know' có thể diễn tả sự nắm bắt thông tin, ví dụ: 'Do you know what time it is?' (Bạn có biết mấy giờ rồi không?).",
            "'Know' cũng có thể dùng trong các cụm từ như 'I don't know' (Tôi không biết) hoặc 'get to know' (làm quen)."
        ],
        "have": [
            "'Have' thường được sử dụng để chỉ sở hữu hoặc có cái gì đó, ví dụ: 'I have a car' (Tôi có một chiếc xe).",
            "'Have' còn có thể chỉ hành động ăn uống, ví dụ: 'I have breakfast at 7 AM' (Tôi ăn sáng lúc 7 giờ sáng).",
            "'Have' còn được dùng trong các câu hỏi và phủ định, ví dụ: 'Do you have any questions?' (Bạn có câu hỏi nào không?).",
            "'Have' cũng có thể dùng trong các cấu trúc như 'have to' (phải), ví dụ: 'I have to go now' (Tôi phải đi ngay bây giờ)."
        ],
        "take": [
            "'Take' diễn tả hành động lấy hoặc nhận cái gì đó, ví dụ: 'I take a book from the shelf' (Tôi lấy một cuốn sách từ kệ).",
            "'Take' cũng có thể dùng để chỉ việc mang cái gì đi, ví dụ: 'Take your umbrella' (Mang theo dù của bạn).",
            "'Take' còn được dùng trong cụm từ 'take a break' (nghỉ giải lao), ví dụ: 'Let's take a break' (Hãy nghỉ một chút).",
            "'Take' cũng diễn tả hành động tham gia vào một hoạt động nào đó, ví dụ: 'I will take part in the competition' (Tôi sẽ tham gia cuộc thi)."
        ],
        "find": [
            "'Find' diễn tả hành động tìm kiếm hoặc phát hiện cái gì đó, ví dụ: 'I found my keys' (Tôi đã tìm thấy chìa khóa của mình).",
            "'Find' còn có thể chỉ sự phát hiện thông tin, ví dụ: 'I found out the truth' (Tôi đã phát hiện ra sự thật).",
            "'Find' còn diễn tả việc đạt được cái gì đó, ví dụ: 'I finally found a solution' (Cuối cùng tôi đã tìm ra giải pháp).",
            "'Find' cũng được sử dụng trong cụm từ 'find it hard' (cảm thấy khó), ví dụ: 'I find it hard to wake up early' (Tôi thấy khó để thức dậy sớm)."
        ],
        "think": [
            "'Think' có nghĩa là suy nghĩ, ví dụ: 'I think about my future' (Tôi suy nghĩ về tương lai của mình).",
            "'Think' còn dùng trong câu hỏi để hỏi ý kiến, ví dụ: 'What do you think of this idea?' (Bạn nghĩ sao về ý tưởng này?).",
            "'Think' còn có thể diễn tả một sự đánh giá, ví dụ: 'I think he is a good teacher' (Tôi nghĩ anh ấy là một giáo viên tốt).",
            "'Think' còn được dùng trong cấu trúc 'think about' (nghĩ về), ví dụ: 'I need to think about it' (Tôi cần suy nghĩ về điều đó)."
        ],
        "come": [
            "'Come' dùng để chỉ sự di chuyển đến một địa điểm, ví dụ: 'She is coming to the party' (Cô ấy sẽ đến bữa tiệc).",
            "'Come' cũng có thể dùng trong các cụm từ như 'come back' (trở lại), ví dụ: 'He came back after two weeks' (Anh ấy đã trở lại sau hai tuần).",
            "'Come' còn có thể chỉ sự xảy ra một sự kiện, ví dụ: 'The storm is coming' (Cơn bão sắp đến).",
            "'Come' cũng có thể diễn tả sự tham gia, ví dụ: 'Come to see me tomorrow' (Đến gặp tôi vào ngày mai)."
        ],
        "call": [
            "'Call' chỉ hành động gọi điện thoại hoặc kêu gọi ai đó, ví dụ: 'I will call you later' (Tôi sẽ gọi cho bạn sau).",
            "'Call' cũng có thể chỉ sự gọi tên, ví dụ: 'She called my name' (Cô ấy gọi tên tôi).",
            "'Call' còn diễn tả hành động mời, ví dụ: 'Call me for dinner' (Gọi tôi vào bữa tối).",
            "'Call' cũng có thể được dùng trong cấu trúc 'call it a day' (kết thúc công việc trong ngày), ví dụ: 'Let’s call it a day' (Chúng ta kết thúc công việc thôi)."
        ],
        "help": [
            "'Help' diễn tả hành động hỗ trợ hoặc giúp đỡ, ví dụ: 'Can you help me with this task?' (Bạn có thể giúp tôi với công việc này không?).",
            "'Help' cũng có thể chỉ sự hỗ trợ trong tình huống khẩn cấp, ví dụ: 'She called for help' (Cô ấy gọi trợ giúp).",
            "'Help' còn được dùng trong các cụm từ như 'help out' (giúp đỡ ai đó), ví dụ: 'I will help you out' (Tôi sẽ giúp bạn).",
            "'Help' cũng có thể diễn tả sự đóng góp vào việc gì đó, ví dụ: 'This will help improve your skills' (Điều này sẽ giúp cải thiện kỹ năng của bạn)."
        ],
        "work": [
            "'Work' diễn tả hành động làm việc, ví dụ: 'I work at a tech company' (Tôi làm việc tại một công ty công nghệ).",
            "'Work' cũng có thể chỉ sự vận hành của một thiết bị, ví dụ: 'The machine works perfectly' (Cái máy hoạt động hoàn hảo).",
            "'Work' còn dùng để chỉ sự nỗ lực, ví dụ: 'I work hard to succeed' (Tôi làm việc chăm chỉ để thành công).",
            "'Work' trong cụm từ 'work on' có nghĩa là làm việc vào một dự án, ví dụ: 'I am working on a new project' (Tôi đang làm việc trên một dự án mới)."
        ],
        "love": [
            "'Love' chỉ tình yêu hoặc sự thích thú đối với ai đó hoặc cái gì đó, ví dụ: 'I love reading books' (Tôi thích đọc sách).",
            "'Love' cũng có thể chỉ tình cảm mạnh mẽ, ví dụ: 'They love each other' (Họ yêu nhau).",
            "'Love' còn diễn tả sự yêu thích một điều gì đó, ví dụ: 'I love this movie' (Tôi yêu bộ phim này).",
            "'Love' trong cấu trúc 'fall in love' có nghĩa là phải lòng ai đó, ví dụ: 'They fell in love quickly' (Họ đã yêu nhau rất nhanh)."
        ],
        "feel": [
            "'Feel' diễn tả cảm giác về một trạng thái nào đó, ví dụ: 'I feel happy today' (Hôm nay tôi cảm thấy vui vẻ).",
            "'Feel' còn dùng để mô tả cảm giác về thể chất, ví dụ: 'I feel tired after the workout' (Tôi cảm thấy mệt mỏi sau khi tập thể dục).",
            "'Feel' cũng có thể diễn tả sự đồng cảm, ví dụ: 'I feel sorry for you' (Tôi cảm thấy tiếc cho bạn).",
            "'Feel' còn được dùng trong cấu trúc 'feel like' (muốn làm gì đó), ví dụ: 'I feel like going to the beach' (Tôi muốn đi biển)."
        ],
        "take": [
            "'Take' diễn tả hành động lấy cái gì đó, ví dụ: 'Take a seat' (Hãy ngồi xuống).",
            "'Take' còn có thể diễn tả hành động mang cái gì đi, ví dụ: 'I will take this book home' (Tôi sẽ mang cuốn sách này về nhà).",
            "'Take' còn dùng trong các cụm từ như 'take part' (tham gia), ví dụ: 'She takes part in the competition' (Cô ấy tham gia cuộc thi).",
            "'Take' cũng có thể chỉ sự chiếm thời gian, ví dụ: 'It takes about an hour to finish' (Mất khoảng một giờ để hoàn thành)."
        ],
        "run": [
            "'Run' thường chỉ hành động chạy, ví dụ: 'I run every morning to stay fit' (Tôi chạy mỗi sáng để giữ sức khỏe).",
            "'Run' cũng có thể chỉ sự vận hành của một hệ thống hoặc máy móc, ví dụ: 'The machine is running smoothly' (Máy móc đang vận hành trơn tru).",
            "'Run' còn có thể chỉ sự lãnh đạo hoặc điều hành, ví dụ: 'She runs the marketing department' (Cô ấy điều hành bộ phận marketing).",
            "'Run' cũng có thể diễn tả việc tham gia một cuộc thi, ví dụ: 'He runs for president' (Anh ấy tham gia tranh cử tổng thống)."
        ],
        "talk": [
            "'Talk' có nghĩa là nói chuyện, ví dụ: 'We talk every day' (Chúng tôi nói chuyện mỗi ngày).",
            "'Talk' cũng có thể chỉ việc thảo luận hoặc trao đổi ý kiến, ví dụ: 'Let’s talk about the project' (Chúng ta hãy nói về dự án).",
            "'Talk' còn được dùng trong các cụm từ như 'talk to' (nói chuyện với ai đó), ví dụ: 'I need to talk to my boss' (Tôi cần nói chuyện với sếp).",
            "'Talk' cũng có thể diễn tả sự giao tiếp không chính thức, ví dụ: 'I’ll talk to you later' (Tôi sẽ nói chuyện với bạn sau)."
        ],
        "ask": [
            "'Ask' có nghĩa là yêu cầu hoặc hỏi, ví dụ: 'I will ask for help' (Tôi sẽ yêu cầu giúp đỡ).",
            "'Ask' cũng có thể chỉ việc yêu cầu thông tin, ví dụ: 'Can I ask you a question?' (Tôi có thể hỏi bạn một câu hỏi không?).",
            "'Ask' còn dùng trong các cụm từ như 'ask for' (yêu cầu cái gì), ví dụ: 'I will ask for the bill' (Tôi sẽ yêu cầu tính tiền).",
            "'Ask' cũng có thể chỉ sự yêu cầu từ ai đó, ví dụ: 'He asked for a raise' (Anh ấy yêu cầu tăng lương)."
        ],
        "believe": [
            "'Believe' có nghĩa là tin tưởng hoặc tin vào điều gì đó, ví dụ: 'I believe in hard work' (Tôi tin vào sự chăm chỉ).",
            "'Believe' còn có thể chỉ sự thừa nhận điều gì đó là đúng, ví dụ: 'I believe he is telling the truth' (Tôi tin rằng anh ấy đang nói sự thật).",
            "'Believe' cũng có thể chỉ niềm tin vào bản thân, ví dụ: 'Believe in yourself' (Hãy tin vào bản thân).",
            "'Believe' còn được sử dụng trong các câu hỏi, ví dụ: 'Do you believe in ghosts?' (Bạn có tin vào ma quái không?)."
        ],
        "read": [
            "'Read' có nghĩa là đọc, ví dụ: 'I read books every day' (Tôi đọc sách mỗi ngày).",
            "'Read' cũng có thể chỉ việc đọc hiểu thông tin, ví dụ: 'I read the news every morning' (Tôi đọc tin tức mỗi sáng).",
            "'Read' còn được dùng trong các câu yêu cầu hoặc mệnh lệnh, ví dụ: 'Please read the instructions carefully' (Vui lòng đọc kỹ hướng dẫn).",
            "'Read' cũng có thể diễn tả việc đọc các tín hiệu, ví dụ: 'I read the signs on the road' (Tôi đọc các biển báo trên đường)."
        ],
        "sleep": [
            "'Sleep' có nghĩa là ngủ, ví dụ: 'I sleep for 8 hours every night' (Tôi ngủ 8 giờ mỗi đêm).",
            "'Sleep' cũng có thể chỉ sự thiếu tỉnh táo, ví dụ: 'I’m so tired, I need to sleep' (Tôi quá mệt, tôi cần ngủ).",
            "'Sleep' còn dùng trong câu hỏi về thời gian ngủ, ví dụ: 'How many hours do you sleep?' (Bạn ngủ bao nhiêu giờ?).",
            "'Sleep' cũng có thể chỉ sự thư giãn, ví dụ: 'I sleep like a baby' (Tôi ngủ ngon như một đứa trẻ)."
        ],
        "help": [
            "'Help' có nghĩa là giúp đỡ, ví dụ: 'Can you help me with this problem?' (Bạn có thể giúp tôi với vấn đề này không?).",
            "'Help' cũng có thể chỉ việc hỗ trợ trong tình huống khẩn cấp, ví dụ: 'She called for help' (Cô ấy gọi trợ giúp).",
            "'Help' còn được dùng trong các cụm từ như 'help out' (giúp đỡ ai đó), ví dụ: 'I will help you out' (Tôi sẽ giúp bạn).",
            "'Help' cũng có thể diễn tả sự đóng góp vào việc gì đó, ví dụ: 'This will help improve your skills' (Điều này sẽ giúp cải thiện kỹ năng của bạn)."
        ],
        "send": [
            "'Send' có nghĩa là gửi, ví dụ: 'I will send you an email' (Tôi sẽ gửi bạn một email).",
            "'Send' cũng có thể chỉ việc chuyển cái gì đó từ một nơi này đến nơi khác, ví dụ: 'Send the package to my office' (Gửi gói hàng đến văn phòng của tôi).",
            "'Send' còn có thể chỉ sự chuyển giao thông tin, ví dụ: 'I will send you the report by tomorrow' (Tôi sẽ gửi bạn báo cáo vào ngày mai).",
            "'Send' cũng có thể chỉ sự chuyển động của tín hiệu hoặc thông điệp, ví dụ: 'Please send my regards to her' (Vui lòng gửi lời chào của tôi tới cô ấy)."
        ],
        "buy": [
            "'Buy' có nghĩa là mua, ví dụ: 'I am going to buy a new phone' (Tôi sẽ mua một chiếc điện thoại mới).",
            "'Buy' cũng có thể chỉ việc trả tiền để sở hữu cái gì đó, ví dụ: 'She buys groceries every week' (Cô ấy mua thực phẩm mỗi tuần).",
            "'Buy' còn có thể chỉ sự ủng hộ một cái gì đó, ví dụ: 'I don’t buy his excuse' (Tôi không tin vào lý do của anh ấy).",
            "'Buy' cũng có thể dùng trong các cụm từ như 'buy into' (chấp nhận hoặc tin vào điều gì đó), ví dụ: 'I don’t buy into that idea' (Tôi không tin vào ý tưởng đó)."
        ],
        "wait": [
            "'Wait' có nghĩa là chờ đợi, ví dụ: 'I will wait for you outside' (Tôi sẽ chờ bạn ngoài cửa).",
            "'Wait' cũng có thể chỉ việc trì hoãn hoặc giữ lại, ví dụ: 'We have to wait for the results' (Chúng ta phải chờ kết quả).",
            "'Wait' còn có thể diễn tả sự chờ đợi trong một trạng thái yên tĩnh, ví dụ: 'I waited patiently for my turn' (Tôi đã kiên nhẫn chờ đợi lượt của mình).",
            "'Wait' còn có thể dùng trong các câu hỏi, ví dụ: 'Are you waiting for someone?' (Bạn có đang chờ ai không?)."
        ],
        "eat": [
            "'Eat' có nghĩa là ăn, ví dụ: 'I eat breakfast at 7 AM' (Tôi ăn sáng lúc 7 giờ sáng).",
            "'Eat' cũng có thể chỉ hành động tiêu thụ thức ăn, ví dụ: 'She eats a lot of vegetables' (Cô ấy ăn nhiều rau).",
            "'Eat' còn có thể dùng trong các cụm từ như 'eat out' (ăn ngoài), ví dụ: 'We usually eat out on weekends' (Chúng tôi thường ăn ngoài vào cuối tuần).",
            "'Eat' cũng có thể diễn tả việc ăn uống trong trạng thái vui vẻ, ví dụ: 'They ate happily at the party' (Họ ăn vui vẻ trong bữa tiệc)."
        ],
        "drive": [
            "'Drive' có nghĩa là lái xe, ví dụ: 'I drive to work every day' (Tôi lái xe đi làm mỗi ngày).",
            "'Drive' cũng có thể chỉ việc điều khiển phương tiện, ví dụ: 'He is learning to drive' (Anh ấy đang học lái xe).",
            "'Drive' còn có thể diễn tả sự thúc đẩy, ví dụ: 'His ambition drives him to succeed' (Khát vọng của anh ấy thúc đẩy anh ấy thành công).",
            "'Drive' cũng có thể dùng trong các câu yêu cầu, ví dụ: 'Can you drive me home?' (Bạn có thể lái xe đưa tôi về nhà không?)."
        ],
        "play": [
            "'Play' có nghĩa là chơi, ví dụ: 'They play football every weekend' (Họ chơi bóng đá mỗi cuối tuần).",
            "'Play' cũng có thể chỉ việc tham gia vào một hoạt động giải trí, ví dụ: 'She loves to play the piano' (Cô ấy thích chơi đàn piano).",
            "'Play' còn có thể chỉ sự tham gia vào một vai trò trong kịch, ví dụ: 'He played the lead role in the play' (Anh ấy đóng vai chính trong vở kịch).",
            "'Play' cũng có thể dùng trong các câu yêu cầu, ví dụ: 'Play some music' (Hãy bật một chút nhạc)."
        ],
        "study": [
            "'Study' có nghĩa là học, ví dụ: 'I study English every day' (Tôi học tiếng Anh mỗi ngày).",
            "'Study' cũng có thể chỉ việc nghiên cứu, ví dụ: 'She is studying medicine at the university' (Cô ấy đang học y khoa ở trường đại học).",
            "'Study' còn có thể chỉ sự chăm chú tìm hiểu một chủ đề, ví dụ: 'I need to study for the test' (Tôi cần học cho kỳ thi).",
            "'Study' cũng có thể dùng trong các câu yêu cầu, ví dụ: 'Study hard for the exam' (Học chăm chỉ cho kỳ thi)."
        ],
        "hiện tại đơn": [
            "Khi nào thì sử dụng thì 'Hiện tại đơn' để diễn tả thói quen hoặc hành động lặp đi lặp lại? Ví dụ: 'Tôi đi học mỗi ngày'.",
            "'Hiện tại đơn' có thể được dùng để diễn tả một sự thật hiển nhiên không? Ví dụ: 'Mặt trời mọc ở phía Đông'.",
            "Câu phủ định trong 'Hiện tại đơn' được tạo như thế nào? Ví dụ: 'Anh ấy không chơi thể thao'.",
            "'Hiện tại đơn' có thể dùng để hỏi về sự thật hay thói quen không? Ví dụ: 'Bạn thích cà phê không?'"
        ],
        "hiện tại tiếp diễn": [
            "'Hiện tại tiếp diễn' được dùng khi nào để chỉ hành động đang xảy ra ở thời điểm nói? Ví dụ: 'Tôi đang ăn tối'.",
            "'Hiện tại tiếp diễn' có thể chỉ sự thay đổi hoặc phát triển không? Ví dụ: 'Trời đang lạnh dần'.",
            "'Hiện tại tiếp diễn' có thể chỉ một kế hoạch trong tương lai không? Ví dụ: 'Chúng tôi đang đi du lịch vào cuối tuần'.",
            "Câu phủ định trong 'Hiện tại tiếp diễn' được tạo như thế nào? Ví dụ: 'Cô ấy không làm việc bây giờ'."
        ],
        "quá khứ đơn": [
            "Khi nào sử dụng thì 'Quá khứ đơn' để diễn tả hành động đã xảy ra và kết thúc trong quá khứ? Ví dụ: 'Tôi đã thăm Hà Nội mùa hè năm ngoái'.",
            "'Quá khứ đơn' có thể được sử dụng khi nào để diễn tả một sự kiện trong quá khứ không? Ví dụ: 'Anh ấy tốt nghiệp năm ngoái'.",
            "'Quá khứ đơn' có thể dùng để hỏi về một sự kiện trong quá khứ không? Ví dụ: 'Bạn đã làm bài tập chưa?'",
            "Làm thế nào để phủ định một câu với 'Quá khứ đơn'? Ví dụ: 'Tôi không đi đến đó hôm qua'."
        ],
        "quá khứ tiếp diễn": [
            "'Quá khứ tiếp diễn' dùng để diễn tả hành động đang xảy ra tại một thời điểm trong quá khứ phải không? Ví dụ: 'Tôi đang đọc sách khi cô ấy gọi điện'.",
            "Thì 'Quá khứ tiếp diễn' có thể chỉ một hành động đang xảy ra song song với một hành động khác trong quá khứ không? Ví dụ: 'Khi tôi đến, họ đang chơi bóng'.",
            "Câu phủ định trong 'Quá khứ tiếp diễn' được tạo như thế nào? Ví dụ: 'Chúng tôi không đang nói chuyện lúc đó'.",
            "'Quá khứ tiếp diễn' có thể được sử dụng để nói về một kế hoạch đã bị gián đoạn trong quá khứ không? Ví dụ: 'Cô ấy đang chuẩn bị bữa tối thì có điện thoại'."
        ],
        "tương lai đơn": [
            "'Tương lai đơn' được sử dụng khi nào để diễn tả một hành động sẽ xảy ra trong tương lai? Ví dụ: 'Tôi sẽ đi du lịch vào mùa hè'.",
            "'Tương lai đơn' có thể được sử dụng để diễn tả quyết định hay lời hứa không? Ví dụ: 'Tôi hứa sẽ giúp bạn'.",
            "'Tương lai đơn' có thể dùng trong các câu hỏi về dự định tương lai không? Ví dụ: 'Bạn sẽ đi đâu vào cuối tuần?'",
            "Câu phủ định trong 'Tương lai đơn' được tạo như thế nào? Ví dụ: 'Tôi sẽ không đi làm vào thứ Bảy'."
        ],
        "tương lai tiếp diễn": [
            "'Tương lai tiếp diễn' được dùng khi nào để diễn tả hành động sẽ đang xảy ra tại một thời điểm trong tương lai? Ví dụ: 'Vào lúc 8 giờ tối mai, tôi sẽ đang xem phim'.",
            "'Tương lai tiếp diễn' có thể chỉ sự kế hoạch đã được lên lịch sẵn không? Ví dụ: 'Chúng tôi sẽ đang họp vào ngày mai'.",
            "'Tương lai tiếp diễn' có thể dùng để diễn tả một sự kiện xảy ra song song với một sự kiện khác trong tương lai không? Ví dụ: 'Khi bạn gọi tôi, tôi sẽ đang làm việc'.",
            "Câu phủ định trong 'Tương lai tiếp diễn' được tạo như thế nào? Ví dụ: 'Tôi sẽ không đang làm bài tập lúc đó'."
        ],
        "hiện tại hoàn thành": [
            "'Hiện tại hoàn thành' dùng để diễn tả hành động đã hoàn thành trong quá khứ nhưng có ảnh hưởng đến hiện tại không? Ví dụ: 'Tôi đã ăn trưa'.",
            "Khi nào sử dụng 'Hiện tại hoàn thành' để diễn tả kinh nghiệm trong quá khứ? Ví dụ: 'Tôi đã từng đi Nhật'.",
            "'Hiện tại hoàn thành' có thể dùng để diễn tả hành động đã xảy ra và vẫn tiếp tục ảnh hưởng đến hiện tại không? Ví dụ: 'Cô ấy đã sống ở đây 5 năm rồi'.",
            "Câu phủ định trong 'Hiện tại hoàn thành' được tạo như thế nào? Ví dụ: 'Tôi chưa làm xong bài tập'."
        ],
        "hiện tại hoàn thành tiếp diễn": [
            "'Hiện tại hoàn thành tiếp diễn' được dùng khi nào để diễn tả hành động bắt đầu trong quá khứ và vẫn tiếp diễn đến hiện tại? Ví dụ: 'Tôi đã học tiếng Anh 5 năm'.",
            "'Hiện tại hoàn thành tiếp diễn' có thể chỉ sự nhấn mạnh vào thời gian của hành động không? Ví dụ: 'Cô ấy đã làm việc ở công ty này hơn 10 năm rồi'.",
            "'Hiện tại hoàn thành tiếp diễn' có thể dùng để chỉ hành động đang gây ra kết quả rõ ràng ở hiện tại không? Ví dụ: 'Tôi đã đợi bạn cả buổi sáng'.",
            "Câu phủ định trong 'Hiện tại hoàn thành tiếp diễn' được tạo như thế nào? Ví dụ: 'Tôi không đã đợi bạn lâu'."
        ],
        "câu điều kiện loại 1": [
            "Câu điều kiện loại 1 được sử dụng để diễn tả tình huống có thể xảy ra trong tương lai nếu điều kiện xảy ra. Ví dụ: 'If it rains, I will stay home'.",
            "Câu điều kiện loại 1 có thể dùng để diễn tả một lời khuyên hoặc đề nghị không? Ví dụ: 'If you study hard, you will pass the exam'.",
            "Câu điều kiện loại 1 có thể được sử dụng để chỉ một sự kiện có thể xảy ra dựa trên điều kiện trong tương lai không? Ví dụ: 'If she arrives on time, we will start the meeting'.",
            "Câu điều kiện loại 1 trong câu phủ định có thể tạo ra như thế nào? Ví dụ: 'If it doesn't rain, we will go to the park'."
        ],
        "câu điều kiện loại 2": [
            "Câu điều kiện loại 2 được sử dụng khi nói về điều kiện giả định trong hiện tại hoặc tương lai. Ví dụ: 'If I were you, I would talk to her'.",
            "Câu điều kiện loại 2 có thể dùng để nói về điều kiện không có thật trong hiện tại không? Ví dụ: 'If he were here, he would help us'.",
            "Câu điều kiện loại 2 có thể dùng để thể hiện sự không chắc chắn về một tình huống không có thật không? Ví dụ: 'If I won the lottery, I would travel the world'.",
            "Câu điều kiện loại 2 phủ định có thể tạo như thế nào? Ví dụ: 'If I didn't know him, I wouldn't trust him'."
        ],
        "câu điều kiện loại 3": [
            "Câu điều kiện loại 3 dùng để nói về tình huống không có thật trong quá khứ, ví dụ: 'If I had studied harder, I would have passed the exam'.",
            "Câu điều kiện loại 3 có thể dùng để diễn tả sự tiếc nuối về điều đã không xảy ra trong quá khứ không? Ví dụ: 'If they had left earlier, they would have caught the train'.",
            "'Câu điều kiện loại 3' có thể sử dụng khi muốn nói về kết quả trong quá khứ nếu điều kiện đã xảy ra không? Ví dụ: 'If you had asked me, I would have helped you'.",
            "Câu điều kiện loại 3 có thể dùng trong câu phủ định như thế nào? Ví dụ: 'If I had known about the problem, I wouldn't have made that mistake'."
        ],
        "câu bị động": [
            "Câu bị động được dùng khi chủ ngữ của câu là người hoặc vật chịu hành động, ví dụ: 'The book was read by him'.",
            "Câu bị động có thể dùng khi nào để nhấn mạnh vào kết quả của hành động thay vì người thực hiện hành động? Ví dụ: 'The car was repaired yesterday'.",
            "Cấu trúc câu bị động trong quá khứ đơn là gì? Ví dụ: 'The letter was sent last week'.",
            "Câu bị động có thể dùng trong các câu hỏi không? Ví dụ: 'Was the report submitted on time?'"
        ],
        "câu phủ định": [
            "Câu phủ định trong thì hiện tại đơn được tạo như thế nào? Ví dụ: 'He does not like coffee'.",
            "Câu phủ định trong thì quá khứ đơn được tạo ra như thế nào? Ví dụ: 'She did not go to the party'.",
            "Câu phủ định trong thì tương lai đơn có thể tạo ra như thế nào? Ví dụ: 'I will not attend the meeting tomorrow'.",
            "Câu phủ định có thể dùng để nhấn mạnh sự không đồng ý không? Ví dụ: 'I do not want to do that'."
        ],
        "câu hỏi đuôi": [
            "Câu hỏi đuôi dùng để xác nhận hoặc hỏi ý kiến của người khác. Ví dụ: 'You are coming to the party, aren't you?'",
            "Câu hỏi đuôi có thể được sử dụng khi nào để hỏi lại thông tin mà người nói đã biết hoặc cho là đúng? Ví dụ: 'She's your sister, isn't she?'",
            "Câu hỏi đuôi trong câu phủ định sẽ như thế nào? Ví dụ: 'You don't like ice cream, do you?'",
            "'Câu hỏi đuôi' có thể dùng trong các câu hỏi ngắn không? Ví dụ: 'They've finished, haven't they?'"
        ],
        "tính từ sở hữu": [
            "Tính từ sở hữu được dùng khi nào để chỉ sự sở hữu của người nói đối với vật gì? Ví dụ: 'This is my book'.",
            "Tính từ sở hữu có thể dùng để nói về sự sở hữu của người khác không? Ví dụ: 'That is his car'.",
            "Câu hỏi sử dụng tính từ sở hữu được tạo như thế nào? Ví dụ: 'Is that your pen?'",
            "'Tính từ sở hữu' có thể dùng trong câu phủ định không? Ví dụ: 'This is not my book'."
        ],
        "cấu trúc so sánh": [
            "Cấu trúc so sánh hơn dùng để so sánh hai đối tượng. Ví dụ: 'This book is more interesting than that one'.",
            "Cấu trúc so sánh nhất được dùng khi nào để chỉ một đối tượng vượt trội hơn tất cả các đối tượng khác? Ví dụ: 'She is the tallest in the class'.",
            "Cấu trúc so sánh ngang bằng có thể được sử dụng như thế nào? Ví dụ: 'She is as tall as her brother'.",
            "'Cấu trúc so sánh' có thể dùng trong câu hỏi không? Ví dụ: 'Is this exam more difficult than the last one?'"
        ],
        "cấu trúc too... to": [
            "Cấu trúc 'too... to' dùng để diễn tả sự không thể thực hiện hành động vì lý do nào đó. Ví dụ: 'This bag is too heavy to carry'.",
            "Cấu trúc 'too... to' có thể dùng để chỉ sự hạn chế không? Ví dụ: 'He is too tired to go out'.",
            "Cấu trúc 'too... to' có thể dùng trong các câu phủ định không? Ví dụ: 'The chair is not too high to sit on'.",
            "'Too... to' có thể dùng trong các câu hỏi không? Ví dụ: 'Is this book too difficult to read?'"
        ],
    }
    
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return "Sorry, I don't understand."

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat_api():
    user_input = request.json.get("user_input")
    print(f"Received user input: {user_input}")
    bot_reply = bot_response(user_input)
    print(f"Bot reply: {bot_reply}")
    # return jsonify({"bot_reply": bot_reply})
    # Dữ liệu trả về dưới dạng JSON
    response_data = {"user_input": user_input, "bot_reply": bot_reply}
    print(f"data: {response_data}")

    #Lưu lại file json
    with open("response.json", "w", encoding="utf-8") as json_file:
        json.dump(response_data, json_file, ensure_ascii=False, indent=4)


    # Trả về phản hồi dưới dạng JSON
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
