import java.util.HashMap;

class LRUCache {

    int[] q;
    int ctr = 0;
    HashMap<Integer, Integer> map = new HashMap<>();
    
    
    public LRUCache(int capacity) {
        q = new int[capacity];
    }
    
    public int get(int key) {
        Integer x = map.get(key);
        
        
        if (x != null && ctr >= 1) {
            // make it recent now by swapping
            int temp = q[ctr];
            q[ctr] = q[ctr-1];
            q[ctr - 1] = temp;
        }
        
        return x == null ? -1 : x;
        
    }
    
    
    
    public void put(int key, int value) {
        if (ctr < q.length) {
            q[ctr] = key;
            map.put(key,value);
            ctr++;
        }
        else {
            map.remove(key);
            ctr--;
        }
        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */