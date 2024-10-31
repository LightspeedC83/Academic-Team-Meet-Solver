package New_Attempts_Java;

import java.util.HashMap;

public class SimpleAdjacencyMap<V,E> implements SimpleGraph<V,E>{
    HashMap<V, HashMap<V,E>> inNeighbors;
    HashMap<V, HashMap<V,E>> outNeighbors;

    public SimpleAdjacencyMap(){
        inNeighbors = new HashMap<>();
        outNeighbors = new HashMap<>();
    }

    @Override
    public void insertVertex(V vertex) {
        if (!outNeighbors.keySet().contains(vertex)) {
			outNeighbors.put(vertex, new HashMap<V, E>());	// edges from v
			inNeighbors.put(vertex, new HashMap<V, E>());		// edges to v
		}
    }

    @Override
    public void insertDirected(V vertex1, V vertex2, E edgeData) throws Exception {
        try{
            outNeighbors.get(vertex1).put(vertex2, edgeData);
        }
        catch(Exception e){
            throw new Exception("one of these verteces doesn't exist");
        }
    }

    @Override
    public void insertUndirected(V vertex1, V vertex2, E edgeData) throws Exception {
        try{
            insertDirected(vertex1, vertex2, edgeData);
            insertDirected(vertex2, vertex1, edgeData);
        }catch(Exception e){
            throw new Exception("One of the verteces does not exist");
        }
    }

    @Override
    public void removeVertex(V vertex) throws Exception {
        try{
            inNeighbors.remove(vertex);
            outNeighbors.remove(vertex);
        } catch(Exception e){
            throw new Exception("vertex does not exist");
        }
    }

    @Override
    public void removeDirected(V vertex1, V vertex2) throws Exception {
        try{
            outNeighbors.get(vertex1).remove(vertex2);
        } catch(Exception e){
            throw new Exception("Vertex doesn't exist");
        }
    }

    @Override
    public void removeUndirected(V vertex1, V vertex2) throws Exception {
        removeDirected(vertex1, vertex2);
        removeDirected(vertex2, vertex1);
    }

    @Override
    public int outDegree(V vertex) throws Exception {
        try{
            int output = 0;
            for(V other : outNeighbors.get(vertex).keySet()){
                output++;
            }
            return output;
        }catch(Exception e){
            throw new Exception("vertex does not exist");
        }
    }

    @Override
    public int inDegree(V vertex) throws Exception {
        try{
            int output = 0;
            for(V other : inNeighbors.get(vertex).keySet()){
                output++;
            }
            return output;
        }catch(Exception e){
                throw new Exception("vertex does not exist");
        }
    }

    @Override
    public Iterable<V> outNeighbors(V vertex) throws Exception {
        try{
            return outNeighbors.get(vertex).keySet();
        }
        catch(Exception e){
            throw new Exception("Vertex does not exist");
        }
    }

    @Override
    public Iterable<V> inNeighbors(V vertex) throws Exception {
        try{
            return inNeighbors.get(vertex).keySet();
        }
        catch(Exception e){
            throw new Exception("Vertex does not exist");
        }
    }

    @Override
    public boolean hasEdge(V vertex1, V vertex2) throws Exception {
        try{
            return outNeighbors.get(vertex1).containsKey(vertex2);
        } catch(Exception e){
            throw new Exception("vertex1 does not exist");
        }
    }
    
}
