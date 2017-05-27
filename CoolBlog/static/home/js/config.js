
$(function(){
  //首页图片切换特效
  var stagenum = 5;
    $('.stag1').hide();
    $('.stage'+stagenum).show();
    var reset = true;
    $(window).scroll(function (event) {
      var y = $(this).scrollTop();
      if(y > 300){  
        if(reset){    
          if(stagenum < 3){
              stagenum = stagenum + 1;
          } else {
            stagenum = 1;
          }
          $('.stag').hide();
          $('.stage'+stagenum).fadeIn(1000);
          reset = false;          
        }
    
      } else {
        reset = true;
      }
    }); 
  // 移动端加载特效
  $(document.body).on('appear', '.type-post', function(e, $affected) {
        // add class called “appeared” for each appeared element
        $(this).addClass("appeared");
      });
      $('.type-post').appear({force_process: true});
  //返回顶部
  $(window).scroll(function(){
    if ($(this).scrollTop() > 300){
      $('#go-top').fadeIn(100);
    }else{
        $('#go-top').fadeOut(100);
      }
  });
  $('#go-top').click(function(event){
    event.preventDefault();
    $('html,body').animate({scrollTop: 0},500);
  });
  $('.loading-title a').click(function() {
  $(this).text('页面载入中……');
  window.location = jQuery(this).attr('href')
  });
  //
  //$('#loading-page').animate({'opacity':0},700,function (){$(this).css('display','none')});
  // 隐藏分页
  $('#pagination').each(function(){
    if($(this).children().length !== 0){
      $(this).show();
    }
  })
  //搜素框
  $('#searchkey').focus(function(){
    $('#searchsubmit').css("background","#f60");
  }).blur(function(){
     $('#searchsubmit').css("background","#c7c7c7");
  });
  //存档页文章收缩/展开

});




