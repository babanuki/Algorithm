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



# s : stack<object> s (�湮 ������Ʈ ����)
# visited : bool visited[N] (������Ʈ �湮 ���� üũ)
# v : vector<vector<object> > v (�׷��� ����)
