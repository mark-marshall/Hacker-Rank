function solution(input) {
    const perms = [];
    const dict = {};
    // clean out non numeric chars, negative nums, and whitespace
    // reverse the resulting array for results in decending order
    const newArr = input
      .split('')
      .filter(
        (char, idx, arr) => !isNaN(char) && arr[idx - 1] !== '-' && char !== ' ',
      )
      .sort()
      .reverse();
    // check there are 3 positive integers remaining
    // return error otherwise
    if (newArr.length !== 3) {
      return 'Error: No integers provided';
    } else {
      // populate the hash table with the 3 possible starting numbers
      newArr.forEach(
        (num, idx) =>
          (dict[idx] = [
            num,
            ...newArr.slice().filter((_, filtIdx) => filtIdx !== idx),
          ]),
      );
      // loop through the keys and push two perms for each number
      for (let key in dict) {
        let arr = dict[key];
        perms.push(arr.join(''));
        perms.push([arr[0], arr[2], arr[1]].join(''));
      }
    }
    // return the perms
    return perms;
  }
  