<template>
  <v-dialog v-model="visible" class="add-grade-popup" persistent>
    <v-card class="asg__card--container">
      <v-form ref="form">
        <v-card-title class="pl-0 asgc__title">Adicionar nota</v-card-title>
        <v-autocomplete
          label="Aluno"
          v-model="studentId"
          item-value="id"
          item-title="name"
          :items="students"
          :rules="[rules.required]"
        />
        <v-autocomplete
          label="Curso"
          v-model="school"
          item-value="value"
          item-title="name"
          :items="schools"
          :rules="[rules.required]"
        />
        <v-autocomplete
          label="Tipo da tarefa"
          v-model="type"
          item-value="value"
          item-title="name"
          :items="taskTypes"
          :rules="[rules.required]"
        />
        <v-text-field
          label="Nota"
          type="number"
          v-model="grade"
          :rules="[rules.required]"
        />
        <v-card-actions class="asgc__actions--buttons">
          <v-btn class="asgca__button--secondary" border @click="close"
            >Fechar</v-btn
          >
          <v-btn
            class="asgca__button--primary"
            :loading="loading"
            @click="addGrade"
            >Adicionar</v-btn
          >
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
</template>

<script>
import api from "../../api/api.js";
import rules from "../../helpers/rules.js";

export default {
  props: {
    showAddGradePopup: {
      required: true,
      type: Boolean,
    },
  },
  data() {
    return {
      school: "",
      schools: [
        { name: "Dados", value: "data" },
        { name: "Tecnologia", value: "technology" },
        { name: "Produto", value: "product" },
      ],
      grade: null,
      loading: false,
      rules,
      studentId: null,
      students: [],
      taskTypes: [
        { name: "Tarefas", value: "tasks" },
        { name: "Desafios", value: "challenges" },
        { name: "Projetos", value: "projects" },
      ],
      type: "",
    };
  },
  async mounted() {
    try {
      this.students = await api.getStudents();
    } catch (error) {
      console.log(error);
    }
  },
  computed: {
    visible() {
      return this.showAddGradePopup;
    },
  },
  methods: {
    async addGrade() {
      const { valid } = await this.$refs.form.validate();
      if (valid) {
        try {
          this.loading = true;
          await api.postGrade(
            this.studentId,
            this.school,
            this.grade,
            this.type
          );
          this.close();
          this.$emit("update");
        } catch (error) {
          console.log(error);
        } finally {
          this.loading = false;
        }
      }
    },
    close() {
      this.$emit("close-add-grade-popup");
    },
  },
};
</script>

<style scoped lang="scss">
.add-grade-popup {
  max-width: 60%;

  .asg__card--container {
    padding: 24px;
    background-color: var(--light-background);

    .asgc__title {
      font-size: 20px;
      font-weight: 800;
      color: var(--darker-blue);
    }

    .asgc__actions--buttons {
      display: flex;
      justify-content: space-between;

      .asgca__button--primary {
        background-color: var(--darker-blue);
        color: white;
      }

      .asgca__button--secondary {
        border: 1px solid black;
      }
    }
  }
}
</style>
