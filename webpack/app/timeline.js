$(function() {
  let my_posts = $("[rel=tooltip]");
  let size = $(window).width();

  for (let i=0; i < my_posts.length; i++) {
    let the_post = $(my_posts[i]);

    if (the_post.hasClass('invert') && size >= 767 ) {
      the_post.tooltip({
        placement: 'left',
      });
    } else {
      the_post.tooltip({
        placement: 'right',
      });
    }
    the_post.css('cursor', 'pointer');
  }
});
