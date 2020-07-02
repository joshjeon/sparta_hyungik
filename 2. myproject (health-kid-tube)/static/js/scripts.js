// 저장 카드 열고 닫기
function openclose() {
    if ($('#posting-box').css('display') == 'block') {
        $('#posting-box').hide();
        $('#btn-posting-box').text('운동카드 포스팅 열기');
    } else {
        $('#posting-box').show();
        $('#btn-posting-box').text('운동카드 포스팅 닫기');
    }
}

// 저장 카드 포스팅
function posting() {
    let type = $('#type').val();
    let memo = $('#memo').val();
    let url = $('#url').val();

    let data = {
        'type_give': type,
        'memo_give': memo,
        'url_give': url
    };

    $.ajax({
        type: "POST",
        url: "/posting",
        data: data,
        success: function (response) {
            if (response['result'] == 'success') {
                alert(response['msg']);
                window.location.reload();
            }
        }
    });
}

// 저장 카드 모두 보여주기
function show_all() {
    $.ajax({
        type: "get",
        url: "/posting/show_all",
        data: {},
        success: function (response) {
            if (response['result'] == 'success') {
                let kidtubes = response['kidtubes'];
                
                for (i = 0; i < kidtubes.length; i++) {

                    let type = kidtubes[i]['type'];
                    let title = kidtubes[i]['title'];
                    let memo = kidtubes[i]['memo'];
                    let url = kidtubes[i]['url'];
                    let image = kidtubes[i]['image'];

                    make_cards(type, title, memo, url, image);
                }
             
            }
        }
    });
}

function make_cards(type, title, memo, url, image) {
    temp_html = `
        <div class="col-md-4">
            <h2>
                (${type} )${title}
            </h2>
            <p>
                ${type}
            <p>
            <p>
                ${memo}
            </p>
            <p>
                <img src="${image}"></img>
            </p>
            <p>
                <a target="_blank" class="btn" href="${url}" >View details »</a>
            </p>
        </div>
    `;
    $('#cards').append(temp_html);
}