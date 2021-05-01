// 일반 방법과 스트림을 이용한 방법
class Solution {
	public static void main(String[] args) {
		int[] arr = {1,1,10,30,2};
		List<Integer> list = new ArrayList<>();
		Set<Integer> set = new HashSet<>();
		
		// Stream을 쓰지 않았을 경우
		for(int i = 0; i<arr.length; i++) { // 배열의 내용을 set에
			set.add(arr[i]);
		}
		
		Iterator<Integer> iter = set.iterator(); // set을 iterator 안에 담기
		
		for(int i = 0; iter.hasNext(); i++) { // iterator를 list 안에
			list.add(iter.next());
		}
		
		list.sort(Comparator.reverseOrder()); // 역정렬
	
		System.out.println("일반 방법을 이용한 출력 : " + list.toString()); 
		
		// Stream을 사용하는 경우
		System.out.println("Stream을 이용한 출력 : " +
				Arrays.stream(arr).boxed() // Stream 생성
				.distinct() // 중복 제거
				.sorted(Comparator.reverseOrder()) // 역정렬
				.collect(Collectors.toList()) // List로 반환
		);
	}
 