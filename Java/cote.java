class Solution {
	public static void main(String[] args) {
		int intSample = 10;
		String stringSample = "20";
		
		String s = Integer.toString(intSample);
		String s2 = String.valueOf(intSample);
		System.out.println("데이터타입 : " +s.getClass().getName() + " 값 : " + s);
		System.out.println("데이터타입 : " +s2.getClass().getName() + " 값 : " + s2);
		
		Integer i = Integer.valueOf(stringSample); // getClass() 사용하려 Integer에 넣음
		int i2 = Integer.valueOf(stringSample);
		System.out.println("데이터타입 : " +i.getClass().getName() + " 값 : " + i);




		/*------------------------------------------------------------------------*/


		char c = 'a';
		String s = "sdf";
		
		// char to String
		String s2 = Character.toString(c);
		System.out.println("char to string : " + s2);
		// String to char
		char c2 = s.charAt(0); // char에는 한 글자의 값만 넣을 수 있음
		System.out.println("string to char : " + c2);
		char[] c3 = s.toCharArray(); // String 전체를 잘라 넣을 경우에는 toCharArray 사용
		System.out.println(c3[0] + "" + c3[1] + "" + c3[2]);
	



		/*------------------------------------------------------------------------*/

		// 배열 최대 최소 최댓값 최대값 최소값 최솟값
		int arr[] = {3,1,40,2,5,237,4};
		
		// for를 이용한 방법 (최소값의 경우에는 if 괄호 방향을 바꿔준다)
		int max = arr[0]; // 배열 길이가 1일 경우를 대비해..
		for (int i = 1; i < arr.length; i++) {
			 if (arr[i] > max) {
				 max = arr[i];
			 }
		}
		System.out.println("For 문을 이용한 방법");
		System.out.println("최대값 : " + max);
		
		// Arrays.sort를 이용한 방법
		System.out.println("Arrays.sort를 이용한 방법");
		Arrays.sort(arr); // 배열 정렬
		System.out.println("최대값 : " + arr[arr.length-1]); // 최대값
		System.out.println("최소값 : " + arr[0]); // 최소값
		
		// Stream을 이용한 방법
		System.out.println("Stream을 이용한 방법");
		// Arrays.stream(배열명) 으로 배열 생성
		System.out.println("최대값 : " + Arrays.stream(arr).max().getAsInt());
		System.out.println("최소값 : " + Arrays.stream(arr).min().getAsInt());



		/*------------------------------------------------------------------------*/

		// 리스트 중복 제거
		List<Integer> list = new ArrayList<>();
		list.add(1);
		list.add(1);
		list.add(2);
		list.add(4);
		
		HashSet<Integer> set = new HashSet<>(); // set은 중복 비허용
		set.addAll(list); // 리스트의 내용을 모두 set에 담음
		list.clear(); // 리스트 안의 내용 전부 버림
		list.addAll(set); // list에 set의 내용을 버림
		// 일반적인 방법
		System.out.println("set을 사용한 방법 : " + list);
		
		// Stream을 사용한 방법
		// list.stream 으로 스트림 생성 
		// .distinct() 로 중복 제거
		// .collect(Collectors.toList()) 로 list 형태로 반환
		System.out.println("Stream을 사용한 방법 : " + list.stream().distinct().collect(Collectors.toList()));


		/*------------------------------------------------------------------------*/

		// List to int 배열
		List<Integer> list = new ArrayList<>();
		list.add(1);
		list.add(2);
		list.add(3);
		
		// for 문을 이용한 방법
		int[] f = new int[list.size()];
		for(int i = 0; i<list.size(); i++) {
			f[i] = list.get(i);
		}
		System.out.println(Arrays.stream(f).boxed().collect(Collectors.toList()));
		
		int[] i = list.stream().mapToInt(Integer::intValue).toArray(); // int 배열로
		Integer[] i2 = list.toArray(new Integer[list.size()]); // Integer 배열로
		
		System.out.println(Arrays.stream(i).boxed().collect(Collectors.toList()));
		System.out.println(Arrays.stream(i2).collect(Collectors.toList()));




		/*------------------------------------------------------------------------*/

		String s = "abcde";
		System.out.println("대문자로 변환 : " + s.toUpperCase());
		
		String s2 = "ABCDE";
		System.out.println("소문자로 변환 : " + s2.toLowerCase());
		
		String s3 = "";
		Pattern ptn = Pattern.compile("a|c|e"); // 패턴 생성
		for(int i = 0; i< s.length(); i++) { // a,c,e일 때만 대문자로
			if(ptn.matcher(String.valueOf(s.charAt(i))).find()) {
				s3 += String.valueOf(s.charAt(i)).toUpperCase();
			} else {
				s3 += String.valueOf(s.charAt(i));
			}
		}
		System.out.println("A,C,E만 대문자 변환 : " + s3);



		/*------------------------------------------------------------------------*/


		String s = "abcde";
		System.out.println("대문자로 변환 : " + s.toUpperCase());
		
		String s2 = "ABCDE";
		System.out.println("소문자로 변환 : " + s2.toLowerCase());
		
		String s3 = "";
		Pattern ptn = Pattern.compile("a|c|e"); // 패턴 생성
		for(int i = 0; i< s.length(); i++) { // a,c,e일 때만 대문자로
			if(ptn.matcher(String.valueOf(s.charAt(i))).find()) {
				s3 += String.valueOf(s.charAt(i)).toUpperCase();
			} else {
				s3 += String.valueOf(s.charAt(i));
			}
		}
		System.out.println("A,C,E만 대문자 변환 : " + s3);




		/*------------------------------------------------------------------------*/

		// int 배열 -> list
		int[] arr = {1,10,20,30,4,5,6,7,8};
		List<Integer> list = Arrays.stream(arr).boxed().collect(Collectors.toList())

		// int <-> String
		int num = 10;
		String str = String.valueOf(num);
		num = Integer.valueOf(str);

		// String -> char[] array
		String s = "abc";
		char[] arr = s.toCharArray();
		// char[] array 정렬
		Arrays.sort(arr);
		Arrays.sort(arr, Collections.reverseOrder());
		// 인덱스 부분 정렬
		Arrays.sort(arr, 0, 4); // index (0,1,2,3) 요소만 정렬


		char c = 'C';
		// 알파벳 숫자인지 확인
		Character.isLetterOrDigit(c);
		// 소문자로 변경
		Character.toLowerCase(c);
		// 대문자로 변경
		Character.toUpperCase(c);
		  
		// String은 immutable 특성 때문에 객체를 조작할 때 마다 새로 객체가 생기는 오버헤드가 발생해서 StringBuilder 가 더 좋은듯??  
		StringBuilder sb = new StringBuilder();
		// 10번째 문자 이후 부터 버리기
		sb.length();
		sb.setLength(10); 
		sb.toString();
		sb.charAt(10);
		sb.deleteCharAt(10);

		// String reverse() 뒤집기 역순 반대
		str = new StringBuilder(str).reverse().toString();

		  

		// 배열 회전
		arr[i][j] = arr[j][len-1-i]				// 90도
		arr[i][j] = arr[len-1-i][len-1-j]	// 180도
		arr[i][j] = arr[len-1-j][i]				// 270도
		  




	}