# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem

# Python
def whatFlavors(cost, money):
  hashMap = {}
  for i,ic in enumerate(cost):
    if ic in hashMap:
      hashMap[ic].append(i+1)
    else:
      hashMap[ic] = [i+1]
  for keys in hashMap:
    if (money-keys) in hashMap:
      if keys == money-keys:
        if len(hashMap[keys]) > 1:
            print(hashMap[keys][0],hashMap[keys][1])
        else:
            continue
      else:
        ans = sorted([hashMap[keys][0],hashMap[money-keys][0]])
        print(ans[0],ans[1])
      break

# JavaScript
const whatFlavors = (cost, money) => {
  const hashMap = {}
  for(var i=0;i<cost.length;i++){
    if(hashMap[cost[i]]){
      hashMap[cost[i]].push(i+1)
    } else {
      hashMap[cost[i]] = [i+1]
    }
  }
  for(var keys in hashMap){
    if(hashMap[money-keys]){
      if(keys == money-keys){
        if(hashMap[keys].length > 1){
          console.log(hashMap[keys][0],hashMap[keys][1])
        } else {
          continue
        }
      } else {
        const ans = hashMap[keys[0]].concat(hashMap[money-keys][0]).sort()
        console.log(ans[0],ans[1])
        break
      }
    }
  }
}
