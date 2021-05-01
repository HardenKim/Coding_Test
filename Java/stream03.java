// 스트림 반환방법 예제
class Solution {
	public static void main(String[] args) {
		int[] arr = {1,1,10,30,2};
		List<Integer> list = new ArrayList<>();
		list.add(1);
		list.add(1);
		list.add(10);
		list.add(30);
		list.add(2);
		
		System.out.println(Arrays.stream(arr).boxed().distinct()); // 반환하기 전
		System.out.println(list.stream().max(Integer::compare)); // 반환하기 전
		
		int[] arr2 = Arrays.stream(arr).distinct().toArray(); // 배열로 반환
		List<Integer> list2 = Arrays.stream(arr).boxed().distinct().collect(Collectors.toList()); // List로 반환
		int val2 = list.stream().max(Integer::compare).get(); // 값 하나 반환
		long val3 = list.stream().collect(Collectors.counting()); // 해당하는 갯수 반환
		
		String[] strArr = {"10", "20", "30"};
		
		// 컬렉션 내 모든 값을 |를 붙여서 반환
		// | 없이 붙여줄려면 ""로 변경
		System.out.println(Arrays.stream(strArr)
				.collect(Collectors.joining("|")));

		Double val4 = Arrays.stream(strArr) // Int 형태로 평균값 반환 (배열이 String일 경우)
				.collect(Collectors.averagingInt(val -> Integer.parseInt(val)));
		Double val5 = Arrays.stream(strArr) // Long 형태로 평균값 반환(배열이 String일 경우)
				.collect(Collectors.averagingDouble(val -> Double.parseDouble(val)));
		Double val6 = Arrays.stream(strArr) // Long 형태로 평균값 반환(배열이 String일 경우)
				.collect(Collectors.averagingLong(val -> Long.parseLong(val)));
		System.out.println("val4 : " + val4); 
		System.out.println("val4 : " + val5);
		System.out.println("val4 : " + val6); // 값 확인
		
		String[] getGroupParti = {"zeebra", "cobra", "cobra", "dog"};
		
		// 이름, 갯수로 Group으로 묶어 담아줌
		Map<String, Long> map = Arrays.stream(getGroupParti)
        			.collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));
		System.out.println("cobra : " + map.get("cobra"));
		
		// 조건에 맞으면 true, 아니면 false의 list 형태로 담아줌
		Map<Boolean, List<String>> map2 = Arrays.stream(getGroupParti)
        			.collect(Collectors.partitioningBy(val -> val == "cobra"));
		
		System.out.println(map2.get(true));
		
	}