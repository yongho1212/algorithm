// 1주일간 늦지않고 출근한 직원에게 포상
// 시는 10=>1000 으로 표현됨
// % 주말은 포함 안됨

// 출근 희망 시각 schedules
// 출근한 시각 timelogs
// 시작요일 startday (월:1)

/**
* 풀이 1
* 스케쥴, 타임로그 map
* startday 1씩늘려나가면서 주말이면 그낭 skip
* => 일부를 실패함 (런타임 아웃 아닌거보니까 일부 케이스 통과가 안되는듯). 왜그럴까?
* => 최악의 상황을 가정해보자.
* => 아무 생각없이 시간을 그냥 숫자로 계산해버림..
* 
*/

function parseTimeStr(timeNum) {
    const timeStr = String(timeNum)
  const padded = timeStr.padStart(4, '0'); 
  const hour = parseInt(padded.slice(0, 2), 10);
  const minute = parseInt(padded.slice(2, 4), 10);
  return hour*60 +minute;
}

function calcTime(timeLog, timeSchedule){
    return parseTimeStr(timeLog) - parseTimeStr(timeSchedule)
}

function solution(schedules, timelogs, startday) {
    var answer = 0;
    for (let team = 0; team < schedules.length; team++){
        for (let time = 0; time < timelogs[team].length; time ++){
            let sday = time + startday
            console.log(team, time, sday)
            if (sday % 7 === 6 || sday % 7 === 0){
                if (time === timelogs[team].length-1) {
                    answer ++
                }
                continue;
            }
            if (calcTime(timelogs[team][time], schedules[team]) > 10) break;
            if (time === timelogs[team].length-1) answer ++;
            continue;
        }
    }
    // console.log(answer)
    return answer;
}