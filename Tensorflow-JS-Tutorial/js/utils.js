function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
async function async_sleep(ms) {
  await sleep(ms);
}
function wasting_time(count){
  for(var n = 0; n < count; n++){
    // do nothing
  }
}
