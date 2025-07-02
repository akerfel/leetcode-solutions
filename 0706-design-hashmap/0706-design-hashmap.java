class MyHashMap {

    Node[] map;

    public MyHashMap() {
        map = new Node[10_000];
        for (int i = 0; i < map.length; i++) {
            map[i] = new Node(-1, -1);
        }
    }

    class Node {
        public int key;
        public int value;
        public Node next;

        public Node(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }
    
    public void put(int key, int value) {
        int index = hash(key);
        Node current = map[index];
        while (current.next != null) {
            if (current.next.key == key) {
                current.next.value = value;
                return;
            }
            current = current.next;
        }
        current.next = new Node(key, value);
    }
    
    public void remove(int key) {
        int index = hash(key);
        Node current = map[index];
        while (current.next != null) {
            if (current.next.key == key) {
                current.next = current.next.next;
                return;
            }
            current = current.next;
        }
    }
    
    public int get(int key) {
        int index = hash(key);
        Node current = map[index];

        while (current.next != null) {
            if (current.next.key == key) {
                return current.next.value;
            }
            current = current.next;
        }
        return -1;
    }

    private int hash(int key) {
        return key % map.length;
    }
    
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */