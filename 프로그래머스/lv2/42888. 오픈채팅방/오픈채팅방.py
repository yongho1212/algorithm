def solution(record):
    user_dict = {}
    message = []
    
    # 1st loop to get the final nickname of each user
    for event in record:
        event_parts = event.split(' ')
        command = event_parts[0]
        uid = event_parts[1]
        
        if command == "Enter" or command == "Change":
            nickname = event_parts[2]
            user_dict[uid] = nickname
            
    # 2nd loop to generate the messages
    for event in record:
        event_parts = event.split(' ')
        command = event_parts[0]
        uid = event_parts[1]

        if command == "Enter":
            message.append(user_dict[uid] + "님이 들어왔습니다.")
            
        elif command == "Leave":
            message.append(user_dict[uid] + "님이 나갔습니다.")
    
    return message
