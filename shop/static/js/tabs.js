$(document).ready(function(){
    $('#rate').click(function () {
        console.log('assdfsdf')
        $.ajax({
            'url':'/ajax/',
            'type':'GET',
            'success':function (data) {
                for (var i=1;1<=data.length;i++){
                    $('#top').append('    <div class="col-md-6">
                    <div class="posts">
                      <div class="row">
                        <div class="col-md-2">
                          <img src="{{media.shop.imageprofile.url}}" class="img-responsive img-thumbnail" alt="">
                        </div>
                        <div class="col-md-9">
                          <h3>{{media.shop.shopname}}</h3>
                          <h5>{{media.title}}</h5>
                          <span class="">1000 likes</span>
                          <a href="#" class="btn btn-info">Like</a>
                        </div>
                        <div class="col-md-1">
                        </div>
                      </div>
                    </div>
                  </div>')
                }
            }
        })
    })
})