// Empty JS for your own code to be here
function openclose() {
    if ($('#posting-box').css('display') == 'block') {
        $('#posting-box').hide();
        $('#btn btn-primary btn-large').text('운동 포스팅박스 열기')
    } else {
        $('#posting-box').show();
        $('#btn btn-primary btn-large').text('운동 포스팅박스 닫기')
    }
}