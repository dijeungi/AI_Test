import { useState } from "react";
import axios from "axios";
import "../css/Input.css"; // 스타일을 따로 넣은 CSS 파일을 import

export default function CharacterMemoryForm() {
  const [character, setCharacter] = useState({
    user_id: 1,
    name: "",
    age: "",
    gender: "",
    relationship: "",
    calling: "",
    tone: "",
    personality: "",
    dialect: "",
    belief: "",
    habit_phrases: "",
    hobbies: "",
    death_year: "",
  });

  const [memory, setMemory] = useState({
    user_id: 1,
    content: "",
    date: "",
    location: "",
    keywords: "",
    emotion: "",
  });

  const handleCharacterSubmit = async () => {
    try {
      await axios.post("http://localhost:8000/character/create", character);
      alert("고인 캐릭터 정보가 저장되었습니다.");
    } catch (err) {
      console.error(err);
      alert("캐릭터 정보 저장 실패.");
    }
  };

  const handleMemorySubmit = async () => {
    try {
      await axios.post("http://localhost:8000/memory/add", memory);
      alert("추억이 저장되었습니다.");
    } catch (err) {
      console.error(err);
      alert("추억 저장 실패.");
    }
  };

  return (
    <div className="form-container">
      <div className="form-card">
        <h2 className="form-title">🧍‍♂️ 고인 캐릭터 정보</h2>
        <div className="form-body">
          {Object.keys(character).map((key) =>
            key !== "death_year" ? (
              <div key={key} className="input-field">
                <label>
                  {key === "name"
                    ? "이름"
                    : key === "age"
                    ? "나이"
                    : key === "gender"
                    ? "성별"
                    : key === "relationship"
                    ? "사용자와의 관계"
                    : key === "calling"
                    ? "호칭"
                    : key === "tone"
                    ? "말투"
                    : key === "personality"
                    ? "성격"
                    : key === "dialect"
                    ? "방언"
                    : key === "belief"
                    ? "종교"
                    : key === "habit_phrases"
                    ? "자주 쓰던 말"
                    : key === "hobbies"
                    ? "취미"
                    : ""}
                </label>
                <input
                  type="text"
                  value={character[key]}
                  onChange={(e) =>
                    setCharacter({ ...character, [key]: e.target.value })
                  }
                  placeholder={`Enter ${key}`}
                  className="input"
                />
              </div>
            ) : null
          )}
          <div className="input-field">
            <label>사망 연도</label>
            <input
              type="number"
              value={character.death_year}
              onChange={(e) =>
                setCharacter({ ...character, death_year: e.target.value })
              }
              placeholder="Enter 사망 연도"
              className="input"
            />
          </div>
          <button onClick={handleCharacterSubmit} className="submit-btn">
            캐릭터 저장
          </button>
        </div>
      </div>

      <div className="form-card">
        <h2 className="form-title">📝 추억 정보</h2>
        <div className="form-body">
          {Object.keys(memory).map((key) =>
            key === "content" ? (
              <div key={key} className="input-field">
                <label>추억 내용</label>
                <textarea
                  value={memory[key]}
                  onChange={(e) =>
                    setMemory({ ...memory, [key]: e.target.value })
                  }
                  placeholder="추억 내용을 입력하세요"
                  className="textarea"
                />
              </div>
            ) : (
              <div key={key} className="input-field">
                <label>
                  {key === "date"
                    ? "날짜"
                    : key === "location"
                    ? "장소"
                    : key === "keywords"
                    ? "키워드"
                    : key === "emotion"
                    ? "감정"
                    : key}
                </label>
                <input
                  type="text"
                  value={memory[key]}
                  onChange={(e) =>
                    setMemory({ ...memory, [key]: e.target.value })
                  }
                  placeholder={
                    key === "date" ? "날짜 입력 (YYYY-MM-DD)" : `Enter ${key}`
                  }
                  className="input"
                />
              </div>
            )
          )}
          <button onClick={handleMemorySubmit} className="submit-btn">
            추억 저장
          </button>
        </div>
      </div>
    </div>
  );
}
