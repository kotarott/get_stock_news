$("#search_btn").on("click", function(){
  const search_keyword = search_word.value
  const news_source = $("#source").val()
  if (search_keyword && news_source) {
    async function run() {
      const news_list = await eel.get_news_title(news_source, search_keyword)();
      if(news_list) {
        create_table(news_list)
      } else {
        alert("エラー")
      }
    }
    run();
  } else {
    alert("ニュースのソースを選択してキーワードを入力してください。")
  }
})

function create_table(items) {
  $("#order_list").remove()
  let html = "<tbody id='order_list'>"
  for (i in items[2]) {
    html += "<tr>"
      html += "<td><input type='checkbox' class='form-check-input'/></td>"
      html += "<td>" + items[2][i] + "</td>"
      html += "<td>"
        html += "<a href='" + items[1][i] +"' target='_blank'>"
          html += items[0][i]
        html += "</a>"
      html += "</td>"
    html += "</tr>"
  }
  html += "</tbody>"
  $(".table").append(html)
}