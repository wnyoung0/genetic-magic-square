<h1>Genetic Magic Square</h1>
<hr>
마방진을 유전 알고리즘으로 생성
<br>
<h2>사용법</h2>
config: json파일의 위치를 입력받는다.<br>
<dl>
  <dt>size</dt>
  <dd>배열의 크기</dd>
  <dt>sums</dt>
  <dd>합이 같도록 할 인덱스들의 목록의 목록(0부터 시작)</dd>
  </dl>
  <br>
score: sums의 내용대로 합을 구한 뒤에 합들의 분산을 출력<br>
genArray: 무작위로 배열 생성<br>
mutate: 무작위로 두 인덱스  변경<br>
(위의 세가지는 개발자가 멍청해서 페키지 임포트 했을때 필요없는데 같이 import된다. 어차피 작동 안되니까 쓰지 말자.)<br>
<br>
MagicArray: 배열<br>
<dl>
  <dt>getArray</dt>
  <dd>배열을 get한다.(deepcopy됨)</dd>
  <dt>setArray</dt>
  <dd>배열을 set한다.</dd>
  <dt>getScore</dt>
  <dd>score함수로 계산한 점수를 반환</dd>
  </dl>
<br>
ArrayManager: 동적으로 여러개의 MagicArray를 생성했을 때 사용<br>
쓰면 MagicArray를 관리하기 편하다.<br>
<dl>
  <dt>addArray</dt>
  <dd>리스트에 MagicArray를 추가</dd>
  <dt>getArray</dt>
  <dd>특정 인덱스의 MagicArray를 반환</dd>
  <dt>sortList</dt>
  <dd>MagicArray에서 getScore의 반환값을 기준으로 오름차순으로 정렬</dd>
  <dt>arrayLen</dt>
  <dd>리스트에 들어있는 MagicArray의 개수를 반환</dd>
  </dl>
<br><br>
<hr>자세한건 알아서 알아내도록 해라
