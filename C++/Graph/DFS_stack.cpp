while(!s.empty()){
    int x=s.top();
    s.pop();
    printf("%d\n", x);
    for(int i=0; i<v[x].size(); i++)
        if(!visited[v[x][i]]){
            s.push(v[x][i]);
            visited[v[x][i]]=true;
    }
}



# s : stack<object> s (방문 오브젝트 보관)
# visited : bool visited[N] (오브젝트 방문 여부 체크)
# v : vector<vector<object> > v (그래프 정보)
