void dfs(int x){
    visited[x]=true;
    for(int i=0; i<v[x].size(); i++)
        if(!visited[v[x][i]])
            dfs(v[x][i]);
    return;
}

# visited : bool visited[N] (������Ʈ �湮 ���� üũ)
# v : vector<vector<object> > v (�׷��� ����)