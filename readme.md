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
  <dt>default</dt>
  <dd>기본 배열. 중간에 프로그램이 멈춰서 다시 시작하거나 라틴 마방진 만들 때 사용</dd>
  </dl>
  <br>
score: sums의 내용대로 합을 구한 뒤에 합들의 분산을 출력<br>
genArray: 무작위로 배열 생성<br>
mutate: 무작위로 두 인덱스  변경<br>

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
<hr>orthogonal은 신경쓰지 마세요(그냥 비워두세요)
