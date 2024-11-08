package New_Attempts_Java;

public interface SimpleGraph<V, E> {
    /**
     * inserts vertex into graph as a node
     * @param vertex - the node to be inserted
     */
    public void insertVertex(V vertex);

    /**
     * inserts directed edge between vertex1 and vertex2
     * @param vertex1 node from which the edge will go
     * @param vertex2 node to which the edge will go
     * @param edgeData the metadata about the edge
     */
    public void  insertDirected(V vertex1, V vertex2, E edgeData) throws Exception;

    /**
     * inserts an undirected edge between vertexes
     * @param vertex one of the vertexes
     * @param vertex2 the other vertex
     * @param edgeData the metadata about the edge
     */
    public void insertUndirected(V vertex, V vertex2, E edgeData) throws Exception;

    /**
     * removes inputted node from the graph
     * @param vertex the node to be removed
     */
    public void removeVertex(V vertex) throws Exception;

    /**
     * removes directed edge between two nodes
     * @param vertex1
     * @param vertex2
     */
    public void removeDirected(V vertex1, V vertex2) throws Exception;

    /**
     * removes undirected edges between two vertices
     * @param vertex1
     * @param vertex2
     * @throws Exception
     */
    public void removeUndirected(V vertex1, V vertex2) throws Exception;

    /**
     * gives degree of the edges coming out of the inputted node
     * @param vertex the node whose out degree shall be counted
     * @return the out degree of that node
     * @throws Exception
     */
    public int outDegree(V vertex) ;
    
    /**
     * gives degree of the edges going into the inputted node
     * @param vertex the node whose in degree shall be counted
     * @return the in degree of that node
     * @throws Exception
     */
    public int inDegree(V vertex) throws Exception;

    /**
     * gets the nodes in the graph that this node has edges pointing to
     * @param vertex the node in question
     * @return an array list of the nodes the inputted node points to
     * @throws Exception
     */
    public Iterable<V> outNeighbors(V vertex) throws Exception;

    /**
     * gets the nodes in the graph that have edges pointing to this node 
     * @param vertex the node in question
     * @return an array list of the nodes that point to the inputted 
     * @throws Exception
     */
    public Iterable<V> inNeighbors(V vertex) throws Exception;

    /**
     * returns true if there is an edge from vertex 1 pointing to vertex 2
     * @param vertex1 the node the from which there may be an edge
     * @param vertex2 the node to which there may be an edge
     * @return a boolean representing edginess from vertex1 to vertex2
     * @throws Exception
     */
    public boolean hasEdge(V vertex1, V vertex2) throws Exception;

    /**
     * returns the value associated with the edge between vertex1 and vertex2
     * @param vertex1 the node from which the edge comes from 
     * @param vertex2 the vertex to which the edge goes
     * @return the value associated with the edge between vertex1 and vertex2
     * @throws Exception
     */
    public E getEdge(V vertex1, V vertex2) throws Exception;
}
