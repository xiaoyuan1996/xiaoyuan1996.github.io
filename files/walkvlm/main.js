<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
<script>
$(document).ready(function() {
    $('.video-container').on('wheel', function(e) {
        e.preventDefault();
        this.scrollLeft += e.originalEvent.deltaY;
    });
});
</script>