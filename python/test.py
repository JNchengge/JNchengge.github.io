def next_state_list(state,a,b,c,l):
    if l==1:
        state=state[::-1]
        state[state.index(a)]=c
        state=state[::-1]
        print(state)
        return state
    else:
        state=next_state_list(state,a,c,b,l-1)
        state=next_state_list(state,a,b,c,1)
        state=next_state_list(state,b,a,c,l-1)
        return state

a,b,c='1','2','3'
next_state_list(['1','1','1'],a,b,c,3)