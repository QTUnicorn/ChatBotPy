from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)

# Hàm trả lời ngẫu nhiên
def bot_response(user_input):
    responses = {
    "Xin chào": [
        "Xin chào",
        "Chào bạn, tôi có thể giúp gì cho bạn."
    ],    
    "Hello": [
        "Xin chào, tôi có thể giúp gì bạn",
        "Chào bạn, tôi có thể giúp bạn học tiếng Anh, bạn sẵn sàng chứ."
    ],
    "Giới thiệu": [
        "Chatbot này giúp bạn luyện tập tiếng Anh, trả lời các câu hỏi liên quan đến từ vựng, ngữ pháp và các chủ đề học tiếng Anh cơ bản.",
        "Tôi là một chatbot, luôn sẵn sàng hỗ trợ bạn cải thiện tiếng Anh qua các câu hỏi và bài tập."
    ],
    "Cách học tiếng Anh": [
        "Học từ vựng và ngữ pháp là cách tốt nhất để xây dựng nền tảng tiếng Anh vững chắc.",
        "Luyện nghe và nói hàng ngày sẽ giúp bạn cải thiện khả năng giao tiếp nhanh chóng.",
        "Sử dụng ứng dụng học tiếng Anh là một phương pháp hiệu quả để luyện tập bất kỳ lúc nào.",
        "Học qua bài hát và phim là cách thú vị để cải thiện kỹ năng nghe và mở rộng từ vựng.",
        "Sử dụng flashcards là một cách tuyệt vời để ghi nhớ và ôn lại từ vựng một cách hiệu quả."
    ],
    "Sách học tiếng Anh": [
    "Sách 'English Grammar in Use' là một trong những cuốn sách nổi tiếng giúp bạn cải thiện ngữ pháp tiếng Anh.",
    "Cuốn 'Word Power Made Easy' là lựa chọn tuyệt vời để nâng cao vốn từ vựng tiếng Anh của bạn.",
    "'English Vocabulary in Use' sẽ giúp bạn học từ vựng theo các chủ đề, rất phù hợp cho người học ở mọi trình độ.",
    "Sách 'The Elements of Style' cung cấp những quy tắc quan trọng giúp bạn viết tiếng Anh một cách rõ ràng và chính xác.",
    "'Listening Practice through Dictation' là cuốn sách hữu ích để bạn cải thiện khả năng nghe và viết chính tả tiếng Anh."
    ],
    "Bạn có thể làm gì": [
        "Tôi có thể giúp bạn luyện tập từ vựng, cấu trúc câu và cải thiện khả năng phát âm tiếng Anh.",
        "Tôi có thể giải thích các khái niệm ngữ pháp, cung cấp câu trả lời cho các câu hỏi học tiếng Anh và giúp bạn luyện tập."
    ],
    "Làm sao để bắt đầu học với bạn": [
        "Bạn chỉ cần đặt câu hỏi về tiếng Anh hoặc yêu cầu tôi giải thích các khái niệm, tôi sẽ giúp bạn ngay lập tức.",
        "Hãy nhập câu hỏi về từ vựng, ngữ pháp hoặc bất kỳ vấn đề tiếng Anh nào bạn muốn tìm hiểu."
    ],
    "set": [
        "Từ 'set' có thể có nghĩa là 'đặt', ví dụ: 'I set the book on the table' (Tôi đặt quyển sách lên bàn).",
        "Từ 'set' cũng có thể có nghĩa là 'bộ', ví dụ: 'I have a set of tools' (Tôi có một bộ dụng cụ).",
        "Ngoài ra, 'set' có thể có nghĩa là 'chuẩn bị', ví dụ: 'Set the alarm for 7 AM' (Cài đặt báo thức lúc 7 giờ sáng)."
    ],
    "run": [
        "Từ 'run' có thể có nghĩa là 'chạy', ví dụ: 'She runs every morning' (Cô ấy chạy mỗi sáng).",
        "Từ 'run' cũng có thể có nghĩa là 'vận hành', ví dụ: 'The machine is running' (Máy móc đang vận hành).",
        "Ngoài ra, 'run' có thể có nghĩa là 'chạy đua', ví dụ: 'He runs for president' (Anh ấy tranh cử tổng thống)."
    ],
    "light": [
        "Từ 'light' có thể có nghĩa là 'ánh sáng', ví dụ: 'The light is bright' (Ánh sáng sáng).",
        "Từ 'light' cũng có thể có nghĩa là 'nhẹ', ví dụ: 'This bag is light' (Cái túi này nhẹ).",
        "Ngoài ra, 'light' có thể có nghĩa là 'thắp sáng', ví dụ: 'Light the candle' (Thắp nến)."
    ],
    "play": [
        "Từ 'play' có thể có nghĩa là 'chơi', ví dụ: 'Children play in the park' (Trẻ em chơi trong công viên).",
        "Từ 'play' cũng có thể có nghĩa là 'biểu diễn', ví dụ: 'She plays the piano beautifully' (Cô ấy chơi đàn piano rất đẹp).",
        "Ngoài ra, 'play' có thể có nghĩa là 'phim hoặc vở kịch', ví dụ: 'They are going to see a play tonight' (Họ sẽ xem một vở kịch tối nay)."
    ],
    "take": [
        "Từ 'take' có thể có nghĩa là 'cầm', ví dụ: 'Take this book to the library' (Mang quyển sách này đến thư viện).",
        "Từ 'take' cũng có thể có nghĩa là 'bắt', ví dụ: 'Take a picture' (Chụp một bức ảnh).",
        "Ngoài ra, 'take' có thể có nghĩa là 'thời gian', ví dụ: 'This task will take an hour' (Công việc này sẽ mất một giờ)."
    ],
    "make": [
    "Từ 'make' có thể có nghĩa là 'làm', ví dụ: 'She makes delicious cakes' (Cô ấy làm bánh rất ngon).",
    "Từ 'make' cũng có thể có nghĩa là 'tạo ra', ví dụ: 'This company makes high-quality products' (Công ty này tạo ra các sản phẩm chất lượng cao).",
    "Ngoài ra, 'make' có thể có nghĩa là 'quyết định', ví dụ: 'We need to make a decision soon' (Chúng ta cần phải quyết định sớm)."
    ],
    "buy": [
        "Từ 'buy' có thể có nghĩa là 'mua', ví dụ: 'I bought a new phone yesterday' (Hôm qua tôi đã mua một chiếc điện thoại mới).",
        "Từ 'buy' cũng có thể có nghĩa là 'đầu tư', ví dụ: 'They bought a lot of stock in the company' (Họ đã đầu tư vào nhiều cổ phiếu của công ty).",
        "Ngoài ra, 'buy' có thể có nghĩa là 'tin tưởng', ví dụ: 'I don’t buy his excuse' (Tôi không tin vào lý do của anh ấy)."
    ],
    "help": [
        "Từ 'help' có thể có nghĩa là 'giúp', ví dụ: 'Can you help me with this task?' (Bạn có thể giúp tôi với công việc này không?).",
        "Từ 'help' cũng có thể có nghĩa là 'hỗ trợ', ví dụ: 'We need to help the community' (Chúng ta cần hỗ trợ cộng đồng).",
        "Ngoài ra, 'help' có thể có nghĩa là 'góp phần', ví dụ: 'This action will help improve the situation' (Hành động này sẽ giúp cải thiện tình hình)."
    ],
    "Làm thế nào để cải thiện từ vựng tiếng Anh của tôi?": [
        "Bạn có thể học từ mới qua các câu ví dụ, tra cứu các từ vựng trong các chủ đề và luyện tập qua các câu hỏi từ chatbot.",
        "Hãy sử dụng từ vựng mới trong các câu của bạn và luyện tập thường xuyên để nhớ lâu hơn."
    ],
    "Làm sao để học ngữ pháp tiếng Anh?": [
        "Hãy học từng cấu trúc ngữ pháp cụ thể và luyện tập qua các ví dụ thực tế.",
        "Đọc các bài viết, câu chuyện ngắn và chú ý đến cách sử dụng các thì và cấu trúc câu."
    ],
    "Câu lệnh cơ bản trong tiếng Anh là gì?": [
        "Câu lệnh cơ bản gồm chủ ngữ, động từ và tân ngữ như: 'I eat apples' (Tôi ăn táo).",
        "Để hỏi một câu đơn giản, bạn có thể sử dụng 'What is your name?' (Tên bạn là gì?)."
    ],
    "Cấu trúc câu hỏi trong tiếng Anh như thế nào?": [
        "Cấu trúc câu hỏi đơn giản là: Wh-question (What, How, Why...) + động từ + chủ ngữ.",
        "Ví dụ: 'What is your name?' (Tên bạn là gì?)."
    ],
    "Câu hỏi 'What is your name?' có ý nghĩa gì?": [
        "Câu hỏi này dùng để hỏi tên của người khác, có nghĩa là 'Tên bạn là gì?'"
    ],
    "Câu hỏi 'How are you?' có nghĩa là gì?": [
        "Câu hỏi này dùng để hỏi về tình trạng sức khỏe hoặc tâm trạng của người khác, có nghĩa là 'Bạn khỏe không?'"
    ],
    "Câu trả lời 'I am fine, thank you' có nghĩa là gì?": [
        "Câu trả lời này có nghĩa là 'Tôi khỏe, cảm ơn bạn'."
    ],
    "Câu 'I like apples' có nghĩa là gì?": [
        "Câu này có nghĩa là 'Tôi thích táo'."
    ],
    "I don’t understand'": [
        "Câu này có nghĩa là 'Tôi không hiểu'."
    ],
    "Can you help me?": [
        "Câu này có nghĩa là 'Bạn có thể giúp tôi không?'"
    ],
    "Làm sao để hỏi giờ trong tiếng Anh?": [
        "Bạn có thể hỏi: 'What time is it?' (Mấy giờ rồi?)."
    ],
    "Cấu trúc câu 'I have a book' là gì?": [
        "Cấu trúc này là một câu khẳng định với chủ ngữ 'I', động từ 'have' và tân ngữ 'a book'."
    ],
    "Làm sao để nói về sở thích trong tiếng Anh?": [
        "Bạn có thể nói: 'I like reading' (Tôi thích đọc sách)."
    ],
    "Câu 'Where do you live?' có nghĩa là gì?": [
        "Câu này có nghĩa là 'Bạn sống ở đâu?'"
    ],
    "Làm sao để yêu cầu sự giúp đỡ trong tiếng Anh?": [
        "Bạn có thể nói: 'Can you help me, please?' (Bạn có thể giúp tôi không?)."
    ],
    "Câu 'I’m sorry' có nghĩa là gì?": [
        "Câu này có nghĩa là 'Tôi xin lỗi'."
    ],
    "Câu 'Thank you' có nghĩa là gì?": [
        "Câu này có nghĩa là 'Cảm ơn bạn'."
    ],
    "Làm sao để mô tả cảm xúc trong tiếng Anh?": [
        "Bạn có thể nói: 'I am happy' (Tôi vui), 'I am sad' (Tôi buồn)."
    ],
    "Câu 'She is my friend' có nghĩa là gì?": [
        "Câu này có nghĩa là 'Cô ấy là bạn của tôi'."
    ],
    "Làm sao để hỏi về sở thích của người khác?": [
        "Bạn có thể hỏi: 'What do you like to do?' (Bạn thích làm gì?)."
    ],
    "Câu 'I am studying English' có nghĩa là gì?": [
        "Câu này có nghĩa là 'Tôi đang học tiếng Anh'."
    ],
    "Câu 'He plays football every day' có nghĩa là gì?": [
        "Câu này có nghĩa là 'Anh ấy chơi bóng đá mỗi ngày'."
    ],
    "Làm sao để mô tả thời tiết trong tiếng Anh?": [
        "Bạn có thể nói: 'It’s sunny' (Trời nắng), 'It’s raining' (Trời mưa)."
    ],
    "Câu 'I’m tired' có nghĩa là gì?": [
        "Câu này có nghĩa là 'Tôi mệt'."
    ],
    "Câu 'Let’s go!' có nghĩa là gì?": [
        "Câu này có nghĩa là 'Chúng ta đi thôi!'"
    ],
    "Câu 'Can I have a coffee?' có nghĩa là gì?": [
        "Câu này có nghĩa là 'Tôi có thể có một cốc cà phê không?'"
    ],
    "Làm sao để khen ngợi ai đó trong tiếng Anh?": [
        "Bạn có thể nói: 'You look great!' (Bạn trông tuyệt lắm!)."
    ],
    "Câu 'I have been to Paris' có nghĩa là gì": [
        "Câu này có nghĩa là 'Tôi đã từng đến Paris'."
    ],
    "Làm sao để nói về một sở thích trong quá khứ": [
        "Bạn có thể nói: 'I used to play football' (Tôi đã từng chơi bóng đá)."
    ],
    "Câu 'It’s my turn' có nghĩa là gì": [
        "Câu này có nghĩa là 'Đến lượt tôi'."
    ],
    "Làm sao để yêu cầu lời khuyên trong tiếng Anh": [
        "Bạn có thể hỏi: 'What do you think?' (Bạn nghĩ sao?)."
    ],
    "Làm sao để cải thiện khả năng phát âm tiếng Anh": [
        "Luyện tập nói với người bản xứ, sử dụng các công cụ phát âm trực tuyến và nghe podcast với phát âm rõ ràng.",
        "Ghi âm giọng nói của bản thân và so sánh với người bản xứ, sử dụng các ứng dụng phát âm và lặp lại từ vựng.",
        "Xem video về phát âm, luyện tập với các câu đố vần và nhờ người khác nhận xét."
    ],
    "Làm sao để học tiếng Anh hiệu quả hơn": [
        "Đặt mục tiêu rõ ràng, luyện tập thường xuyên và đắm mình vào ngôn ngữ qua phim ảnh và sách.",
        "Lập kế hoạch học tập, tập trung vào những phần bạn gặp khó khăn và ôn lại thường xuyên.",
        "Luyện nói tiếng Anh với người khác, nghe các nội dung tiếng Anh mỗi ngày và đọc sách bằng tiếng Anh."
    ],
    "Làm sao để sử dụng tiếng Anh trong công việc hàng ngày": [
        "Luyện nói tiếng Anh với đồng nghiệp, sử dụng từ vựng liên quan đến công việc và xem các video tiếng Anh về nghề nghiệp của bạn.",
        "Tham gia các cuộc họp bằng tiếng Anh, ghi chú bằng tiếng Anh và viết email bằng tiếng Anh.",
        "Sử dụng tiếng Anh trong các công việc hàng ngày, tham gia các buổi hội thảo bằng tiếng Anh và đặt nhắc nhở bằng tiếng Anh để đắm chìm trong ngôn ngữ."
    ],
    "Làm sao để học tiếng Anh qua bài hát": [
        "Chọn các bài hát có lời rõ ràng, tra cứu nghĩa của các từ mới và hát theo để luyện phát âm.",
        "Nghe các bài hát, lặp lại lời bài hát và tập trung học từ vựng mới qua âm nhạc.",
        "Chọn các bài hát bạn yêu thích, ghi lại lời bài hát và luyện hát để cải thiện khả năng nói trôi chảy."
    ],
    "Làm sao để cải thiện kỹ năng nghe trong tiếng Anh": [
        "Nghe podcast, xem các chương trình truyền hình có phụ đề tiếng Anh và luyện tập với các bài tập nghe.",
        "Xem video tiếng Anh không có phụ đề, nghe các giọng điệu khác nhau và luyện nghe với nhiều chủ đề khác nhau.",
        "Sử dụng các ứng dụng nghe, xem phim bằng tiếng Anh và nghe các bản tin để cải thiện khả năng hiểu."
    ],
    "Làm sao để học tiếng Anh một cách sáng tạo": [
        "Sử dụng thẻ flashcards, tạo sơ đồ tư duy và thử học qua kể chuyện hoặc đóng vai.",
        "Biến việc học trở nên thú vị bằng cách sử dụng trò chơi ngôn ngữ, xem các video sáng tạo và luyện tập qua viết sáng tạo.",
        "Học qua vẽ, sử dụng công cụ trực quan và kết hợp âm nhạc hoặc nghệ thuật vào việc học."
    ],
    "Làm sao để hiểu các cấu trúc ngữ pháp phức tạp trong tiếng Anh?": [
        "Chia nhỏ chúng thành các phần dễ hiểu hơn, luyện tập với các ví dụ và tìm kiếm lời giải thích từ tài liệu ngữ pháp.",
        "Học qua ngữ cảnh, sử dụng bài tập để củng cố quy tắc ngữ pháp và học cùng giáo viên để làm rõ vấn đề.",
        "Tập trung vào việc hiểu một quy tắc tại một thời điểm, sử dụng ví dụ thực tế và luyện tập qua bài tập."
    ],
    "Làm sao để làm quen với tiếng Anh chuyên ngành": [
        "Đọc các bài báo hoặc sách liên quan đến lĩnh vực của bạn, học các thuật ngữ chuyên ngành và tham gia các hội thảo hoặc khóa học chuyên ngành bằng tiếng Anh.",
        "Học từ vựng chuyên ngành, đọc các bài nghiên cứu và giao tiếp với các chuyên gia trong lĩnh vực của bạn.",
        "Tham gia các cộng đồng trực tuyến trong lĩnh vực của bạn, tham gia các khóa học chuyên ngành và luyện tập sử dụng thuật ngữ chuyên môn trong công việc."
    ],
    "Làm sao để duy trì sự kiên nhẫn khi học tiếng Anh": [
        "Đặt mục tiêu nhỏ, dễ đạt được, theo dõi tiến độ và tự thưởng khi hoàn thành các mốc quan trọng.",
        "Tập trung vào tiến bộ thay vì hoàn hảo, nghỉ ngơi khi cần thiết và duy trì động lực với một lịch trình học tập hợp lý.",
        "Ăn mừng những chiến thắng nhỏ, duy trì sự đều đặn và nhắc nhở bản thân về mục tiêu học ngôn ngữ dài hạn."
    ],
    "Làm sao để cải thiện kỹ năng đọc tiếng Anh": [
        "Đọc nhiều loại văn bản, tóm tắt lại những gì đã đọc và mở rộng vốn từ vựng qua ngữ cảnh.",
        "Chọn những tài liệu đọc thú vị, đánh dấu các từ mới và luyện tập kỹ năng đọc lướt và quét nhanh.",
        "Đọc thường xuyên, luyện tập nhận diện ý chính và học từ vựng mới qua ngữ cảnh."
    ]
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
