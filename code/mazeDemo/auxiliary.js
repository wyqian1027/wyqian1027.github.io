// random number
var getRandomNumber = function (width){
    return Math.floor(Math.random() * width);
};

// random permutation of array
var permutate = function(array){
    for (var i = 0; i < array.length; i++)
    {
       var swpIdx = i + Math.floor(Math.random() * (array.length - i));
       var tmp = array[i];
       array[i] = array[swpIdx];
       array[swpIdx] = tmp;
    }
};

