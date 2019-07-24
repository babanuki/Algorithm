void dfs(int x){
    visited[x]=true;
    for(int i=0; i<v[x].size(); i++)
        if(!visited[v[x][i]])
            dfs(v[x][i]);
    return;
}

# visited : bool visited[N] (오브젝트 방문 여부 체크)
# v : vector<vector<object> > v (그래프 정보)