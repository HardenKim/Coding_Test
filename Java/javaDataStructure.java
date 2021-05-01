import.java.util.*;

class Solution {
	public static void main(String[] args) {

		// Queue (FIFO)
		import java.util.LinkedList; //import
		import java.util.Queue; //import
		Queue<Integer> queue = new LinkedList<>(); //int형 queue 선언, linkedlist 이용
		Queue<String> queue = new LinkedList<>(); //String형 queue 선언, linkedlist 이용

		Queue<Integer> queue = new LinkedList<>(); //int형 queue 선언
		queue.add(1);     // queue에 값 1 추가
		queue.add(2);     // queue에 값 2 추가
		queue.offer(3);   // queue에 값 3 추가


		Queue<Integer> queue = new LinkedList<>(); //int형 queue 선언
		queue.offer(1);     // queue에 값 1 추가
		queue.offer(2);     // queue에 값 2 추가
		queue.offer(3);     // queue에 값 3 추가
		queue.peek();       // queue의 첫번째 값 참조
		queue.poll();       // queue에 첫번째 값을 반환하고 제거 비어있다면 null
		queue.remove();     // queue에 첫번째 값 제거
		queue.clear();      // queue 초기화


		/*------------------------------------------------------------------------*/

		// Priority Queue (정렬)
		//int형 priorityQueue 선언 (우선순위가 낮은 숫자 순)
		PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();

		//int형 priorityQueue 선언 (우선순위가 높은 숫자 순)
		PriorityQueue<Integer> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());

		//String형 priorityQueue 선언 (우선순위가 낮은 숫자 순)
		PriorityQueue<String> priorityQueue = new PriorityQueue<>(); 

		//String형 priorityQueue 선언 (우선순위가 높은 숫자 순)
		PriorityQueue<String> priorityQueue = new PriorityQueue<>(Collections.reverseOrder());


		priorityQueue.add(2);     // priorityQueue 값 1 추가
		priorityQueue.add(1);     // priorityQueue 값 2 추가
		priorityQueue.offer(3);   // priorityQueue 값 3 추가

		priorityQueue.peek();       // priorityQueue에 첫번째 값 참조 = 1
		priorityQueue.poll();       // priorityQueue에 첫번째 값을 반환하고 제거 비어있다면 null
		priorityQueue.remove();     // priorityQueue에 첫번째 값 제거
		priorityQueue.clear();      // priorityQueue에 초기화


		// stack
		Stack<Integer> stack = new Stack<>(); //int형 스택 선언
		Stack<String> stack = new Stack<>(); //char형 스택 선언

		stack.push(1);     // stack에 값 1 추가
		stack.push(2);     // stack에 값 2 추가
		stack.push(3);     // stack에 값 3 추가

		stack.peek();     // stack의 가장 상단의 값 출력
		stack.pop();       // stack에 값 제거
		stack.clear();     // stack의 전체 값 제거 (초기화)	

		stack.size();      // stack의 크기 출력 : 2
		stack.empty();     // stack이 비어있는제 check (비어있다면 true)
		stack.contains(1) // stack에 1이 있는지 check (있다면 true)



		/*------------------------------------------------------------------------*/

		// HashMap
		HashMap<String,String> map1 = new HashMap<String,String>();//HashMap생성
		HashMap<String,String> map2 = new HashMap<>();//new에서 타입 파라미터 생략가능
		HashMap<String,String> map3 = new HashMap<>(map1);//map1의 모든 값을 가진 HashMap생성
		HashMap<String,String> map4 = new HashMap<>(10);//초기 용량(capacity)지정
		HashMap<String,String> map5 = new HashMap<>(10, 0.7f);//초기 capacity,load factor지정
		HashMap<String,String> map6 = new HashMap<String,String>(){{//초기값 지정
		    put("a","b");
		}};


		HashMap<Integer,String> map = new HashMap<>();//new에서 타입 파라미터 생략가능
		map.put(1,"사과"); //값 추가
		map.put(2,"바나나");
		map.put(3,"포도");

		map.remove(1); //key값 1 제거
		map.clear(); //모든 값 제거

		System.out.println(map); //전체 출력 : {1=사과, 2=바나나, 3=포도}
		System.out.println(map.get(1));//key값 1의 value얻기 : 사과
				
		//entrySet() 활용
		for (Entry<Integer, String> entry : map.entrySet()) {
		    System.out.println("[Key]:" + entry.getKey() + " [Value]:" + entry.getValue());
		}
		//[Key]:1 [Value]:사과
		//[Key]:2 [Value]:바나나
		//[Key]:3 [Value]:포도

		//KeySet() 활용
		for(Integer i : map.keySet()){ //저장된 key값 확인
		    System.out.println("[Key]:" + i + " [Value]:" + map.get(i));
		}
		//[Key]:1 [Value]:사과
		//[Key]:2 [Value]:바나나
		//[Key]:3 [Value]:포도


		//entrySet().iterator()
		Iterator<Entry<Integer, String>> entries = map.entrySet().iterator();
		while(entries.hasNext()){
		    Map.Entry<Integer, String> entry = entries.next();
		    System.out.println("[Key]:" + entry.getKey() + " [Value]:" +  entry.getValue());
		}
		//[Key]:1 [Value]:사과
		//[Key]:2 [Value]:바나나
		//[Key]:3 [Value]:포도
				
		//keySet().iterator()
		Iterator<Integer> keys = map.keySet().iterator();
		while(keys.hasNext()){
		    int key = keys.next();
		    System.out.println("[Key]:" + key + " [Value]:" +  map.get(key));
		}
		//[Key]:1 [Value]:사과
		//[Key]:2 [Value]:바나나
		//[Key]:3 [Value]:포도


		/*------------------------------------------------------------------------*/

		// ArrayList
		ArrayList list = new ArrayList();//타입 미설정 Object로 선언된다.
		ArrayList<Student> members = new ArrayList<Student>();//타입설정 Student객체만 사용가능
		ArrayList<Integer> num = new ArrayList<Integer>();//타입설정 int타입만 사용가능
		ArrayList<Integer> num2 = new ArrayList<>();//new에서 타입 파라미터 생략가능
		ArrayList<Integer> num3 = new ArrayList<Integer>(10);//초기 용량(capacity)지정
		ArrayList<Integer> list2 = new ArrayList<Integer>(Arrays.asList(1,2,3));//생성시 값추가

		ArrayList<Integer> list = new ArrayList<Integer>();
		list.add(3); //값 추가
		list.add(null); //null값도 add가능
		list.add(1,10); //index 1뒤에 10 삽입

		list.remove(1);  //index 1 제거
		list.clear();  //모든 값 제거

		System.out.println(list.size()); //list 크기 : 3

		System.out.println(list.contains(1)); //list에 1이 있는지 검색 : true
		System.out.println(list.indexOf(1)); //1이 있는 index반환 없으면 -1


		for(Integer i : list) { //for문을 통한 전체출력
		    System.out.println(i);
		}

		Iterator iter = list.iterator(); //Iterator 선언 
		while(iter.hasNext()){//다음값이 있는지 체크
		    System.out.println(iter.next()); //값 출력
		}


		/*------------------------------------------------------------------------*/

		String s = "abcdefg";
        StringBuilder sb = new StringBuilder(s); // String -> StringBuilder
		
        System.out.println("처음 상태 : " + sb); //처음상태 : abcdefg
        System.out.println("문자열 String 변환 : " + sb.toString()); //String 변환하기
        System.out.println("문자열 추출 : " + sb.substring(2,4)); //문자열 추출하기
        System.out.println("문자열 추가 : " + sb.insert(2,"추가")); //문자열 추가하기
        System.out.println("문자열 삭제 : " + sb.delete(2,4)); //문자열 삭제하기
        System.out.println("문자열 연결 : " + sb.append("hijk")); //문자열 붙이기
        System.out.println("문자열의 길이 : " + sb.length()); //문자열의 길이구하기
        System.out.println("용량의 크기 : " + sb.capacity()); //용량의 크기 구하기
        System.out.println("문자열 역순 변경 : " + sb.reverse()); //문자열 뒤집기
        System.out.println("마지막 상태 : " + sb); //마지막상태 : kjihgfedcba



