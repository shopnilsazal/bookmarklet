(function () {
    var likes = document.querySelector('#likes');
    var likesCount = document.querySelector('#likes-count');
    var suggestion = document.querySelector('#suggestion');
    var req;

    if (likes) {
        likes.addEventListener('click', function () {
            likeCountRequestHandler();
        });
    }

    if (suggestion) {
        suggestion.addEventListener('keyup', function () {
            suggestionRequestHandler();
        });
    }


    function suggestionRequestHandler() {
        var suggestion_text = suggestion.value;

        req = new XMLHttpRequest();
        req.onreadystatechange = getSuggestedCategoryList;
        req.open('GET', '/bookmarks/suggest/?suggestion=' + suggestion_text, true);
        req.send();
    }

    function getSuggestedCategoryList() {
        var categories = document.querySelector('#suggested-category-list');

        if (req.readyState === XMLHttpRequest.DONE) {
            if (req.status === 200) {
                var responseObj = req.responseText;
                var category = JSON.parse(responseObj);
                if (category) {
                    while (categories.firstChild) {
                        categories.removeChild(categories.firstChild);
                    }
                    for (var key in category) {
                        var item = document.createElement('li');
                        var link = document.createElement('a');
                        link.innerText = category[key];
                        link.href = '/bookmarks/category/' + key;
                        item.appendChild(link);
                        categories.appendChild(item);

                    }
                }

            } else {
                console.log('There was a problem with the request.');
            }
        }
    }


    function likeCountRequestHandler() {
        var catId = likes.dataset.catid;

        req = new XMLHttpRequest();
        req.onreadystatechange = increaseLikeCount;
        req.open('GET', '/bookmarks/like/?category_id=' + catId, true);
        req.send();
    }

    function increaseLikeCount() {
        if (req.readyState === XMLHttpRequest.DONE) {
            if (req.status === 200) {
                likesCount.textContent = req.responseText + ' likes';
            } else {
                console.log('There was a problem with the request.');
            }
        }
    }


}());
