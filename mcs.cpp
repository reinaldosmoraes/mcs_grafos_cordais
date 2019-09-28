#include <cstdio>
#include <cstring>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

const int MAX_NUMBER_OF_VERTICES = 100;
int numberOfVertices, numberOfEdges;

set< pair<int, int> > edges;
vector<int> adj[MAX_NUMBER_OF_VERTICES];
int order[MAX_NUMBER_OF_VERTICES], cnt[MAX_NUMBER_OF_VERTICES], pos[MAX_NUMBER_OF_VERTICES];

/*  Algoritmo MCS (Maximum Cardinality Search)
    O algoritmo MCS retorna uma ordenação dos vértices de um grafo que é uma ordem de 
    construção simplicial do mesmo se, e somente se, ele é cordal. */
void mcs(int v = 0) {   
    set< pair<int, int> > s;
    int k = 0;

    memset(pos, -1, sizeof(pos));

    s.insert(make_pair(0, v));
    while(s.empty() == false) {
        pair<int, int> p = *s.begin();
        s.erase(s.begin());

        int x = p.second;
        pos[x] = k;
        order[k++] = x;

        for(int i = 0; i < adj[x].size(); i++) {
            int y = adj[x][i];
            if(pos[y] != -1) continue;

            if(cnt[y]) s.erase(make_pair(cnt[y], y));
            s.insert(make_pair(--cnt[y], y));
        }
    }
}

bool isChordal(void) {   
    for(int j = 1; j < numberOfVertices; j++) {
        int u = -1;
	    int v = order[j];
        
        for(int i = 0; i < adj[v].size(); i++) {
            int y = adj[v][i];
            if(pos[y] < pos[v]) {
                if(u == -1) u = y;
                else if(pos[u] < pos[y]) u =y;
	        }
        }

        for(int i = 0; i < adj[v].size(); i++) {
            int y = adj[v][i];
	        if(y == u) continue;
	        if(pos[y] >= pos[u]) continue;
            if(edges.count(make_pair(u, y)) == 0)
                return false;
        }
    }
    return true;
}

int main(void) {
    printf("Numero de vertices: ");
    scanf("%d", &numberOfVertices);
    printf("Numero de arestas: ");
    scanf("%d", &numberOfEdges);

    printf("Digite o par de vertices quem formam cada aresta separados por espaco.\n");
    for(int i = 0; i < numberOfEdges; i++) {
        int firstVertice, secondVertice;
        printf("Aresta %d: ", i + 1);
        scanf("%d %d", &firstVertice, &secondVertice);
        adj[firstVertice].push_back(secondVertice);
        adj[secondVertice].push_back(firstVertice);
        edges.insert(make_pair(firstVertice, secondVertice));
        edges.insert(make_pair(secondVertice, firstVertice));
    }

    mcs();         

    if(isChordal()) {
        printf("O grafo é cordal");
    } else {
        printf("O grafo NAO é cordal");
    }
    return 0;
}
